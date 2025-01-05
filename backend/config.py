
import os

TRELLO_API_KEY = os.environ['TRELLO_API_KEY']
TRELLO_API_TOKEN = os.environ['TRELLO_API_TOKEN']

STANDARD_LISTS = [
    "Backlog",
    "Planning",
    "In Progress",
    "Review",
    "Done"
]

PRIORITY_LABELS = {
    "High": "red",
    "Medium": "yellow",
    "Low": "green"
}

TASK_TEMPLATES = {
    "feature": {
        "description": "## Description\n\n## Acceptance Criteria\n\n## Technical Notes",
        "checklist": [
            "Design review",
            "Implementation",
            "Tests",
            "Documentation",
            "Code review"
        ]
    },
    "bug": {
        "description": "## Bug Description\n\n## Steps to Reproduce\n\n## Expected Behavior\n\n## Actual Behavior",
        "checklist": [
            "Reproduce bug",
            "Root cause analysis",
            "Fix implementation",
            "Test fix",
            "Regression testing"
        ]
    }
}

REMINDER_DAYS_BEFORE = 2
DAILY_REVIEW_TIME = "09:00"
EVENING_REPORT_TIME = "17:00"
DEFAULT_TASK_DUE_DAYS = 7
BOARD_ID = os.environ.get('TRELLO_BOARD_ID', '')
