
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule
import time

class AutomatedReporting:
    def __init__(self, email_config):
        self.email_config = email_config
        self.schedule = schedule
        self.report_templates = {
            'daily': 'templates/daily_report.html',
            'weekly': 'templates/weekly_report.html'
        }
        
    def generate_custom_report(self, template_name, data):
        with open(self.report_templates[template_name]) as f:
            template = f.read()
        return template.format(**data)
        
    def schedule_all_reports(self):
        self.schedule.every().day.at("09:00").do(self.generate_daily_report)
        self.schedule.every().monday.at("08:00").do(self.generate_weekly_report)
        while True:
            self.schedule.run_pending()
            time.sleep(60)
        
    def generate_daily_report(self):
        report_data = self._collect_daily_data()
        html_report = self._create_html_report(report_data)
        self._send_email_report(html_report)
        
    def _collect_daily_data(self):
        # Collect metrics for the last 24 hours
        end_time = datetime.now()
        start_time = end_time - timedelta(days=1)
        return {
            'anomalies': self._get_anomalies(start_time, end_time),
            'performance': self._get_performance_metrics(start_time, end_time),
            'alerts': self._get_alerts(start_time, end_time)
        }
        
    def schedule_reports(self):
        self.schedule.every().day.at("00:00").do(self.generate_daily_report)
        while True:
            self.schedule.run_pending()
            time.sleep(60)
