"""
Code quality checker for FES platform
Analyzes code style, complexity, and potential issues
"""

import ast
import logging
from pathlib import Path
from typing import Dict, List, Any
import json
from datetime import datetime

class CodeAnalyzer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.metrics = {}
        
    def analyze_complexity(self, node: ast.AST) -> int:
        """
        Calculate cyclomatic complexity of AST node
        """
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.AsyncFor,
                                ast.ExceptHandler, ast.AsyncWith,
                                ast.With, ast.Assert)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity
    
    def analyze_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Analyze a single Python file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            tree = ast.parse(content)
            
            # Collect metrics
            functions = []
            classes = []
            complexity = 0
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_complexity = self.analyze_complexity(node)
                    functions.append({
                        'name': node.name,
                        'complexity': func_complexity,
                        'line_number': node.lineno
                    })
                    complexity += func_complexity
                elif isinstance(node, ast.ClassDef):
                    classes.append({
                        'name': node.name,
                        'methods': len([n for n in node.body if isinstance(n, ast.FunctionDef)]),
                        'line_number': node.lineno
                    })
                    
            return {
                'path': str(file_path.relative_to(self.project_root)),
                'complexity': complexity,
                'functions': functions,
                'classes': classes,
                'lines': len(content.splitlines())
            }
            
        except Exception as e:
            logging.error(f"Failed to analyze {file_path}: {str(e)}")
            return None
    
    def analyze_project(self) -> Dict[str, Any]:
        """
        Analyze entire project codebase
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'files': [],
            'total_complexity': 0,
            'total_functions': 0,
            'total_classes': 0,
            'total_lines': 0
        }
        
        for path in self.project_root.rglob('*.py'):
            if 'venv' in str(path) or '.git' in str(path):
                continue
                
            file_results = self.analyze_file(path)
            if file_results:
                results['files'].append(file_results)
                results['total_complexity'] += file_results['complexity']
                results['total_functions'] += len(file_results['functions'])
                results['total_classes'] += len(file_results['classes'])
                results['total_lines'] += file_results['lines']
        
        self.metrics = results
        return results
    
    def export_results(self, output_path: str) -> None:
        """
        Export analysis results to JSON file
        """
        with open(output_path, 'w') as f:
            json.dump(self.metrics, f, indent=2)
            
def analyze_code_quality():
    """
    Run code quality analysis and export results
    """
    try:
        analyzer = CodeAnalyzer(Path.cwd())
        results = analyzer.analyze_project()
        
        # Export results
        results_dir = Path('code_quality')
        results_dir.mkdir(exist_ok=True)
        analyzer.export_results(str(results_dir / f'analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'))
        
        return results
        
    except Exception as e:
        logging.error(f"Code analysis failed: {str(e)}")
        return None

if __name__ == '__main__':
    analyze_code_quality()
