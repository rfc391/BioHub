
import schedule
import time
from datetime import datetime
from trello_manager import TrelloManager
from notification_manager import NotificationManager
import config

class ProjectAutomator:
    def __init__(self):
        self.trello = TrelloManager()
        self.notifier = NotificationManager()

    def automate_board(self, board_id):
        board = self.trello.client.get_board(board_id)
        
        schedule.every().day.at(config.DAILY_REVIEW_TIME).do(self.daily_review, board)
        schedule.every().day.at(config.EVENING_REPORT_TIME).do(self.evening_report, board)
        schedule.every().monday.at("10:00").do(self.weekly_metrics, board)

        while True:
            schedule.run_pending()
            time.sleep(60)

    def daily_review(self, board):
        due_tasks = self.trello.get_tasks_due_soon(board)
        if due_tasks:
            message = "Tasks due soon:\n"
            for task in due_tasks:
                message += f"- {task.name} (Due: {task.due_date})\n"
            self.notifier.send_email_notification(
                "Daily Task Review", 
                message
            )

    def evening_report(self, board):
        metrics = self.trello.get_project_metrics(board)
        report = f"Daily Project Report ({datetime.now().date()})\n"
        report += f"Total Tasks: {metrics['total_tasks']}\n"
        report += f"Completed Today: {metrics['tasks_by_list'].get('Done', 0)}\n"
        report += f"Overdue Tasks: {metrics['overdue_tasks']}\n"

        self.notifier.send_email_notification(
            "Evening Project Report",
            report
        )

    def weekly_metrics(self, board):
        metrics = self.trello.get_project_metrics(board)
        report = "Weekly Project Metrics\n"
        report += f"Completion Rate: {(metrics['completed_tasks']/metrics['total_tasks'])*100:.1f}%\n"
        report += "\nTasks by Priority:\n"
        for priority, count in metrics['tasks_by_priority'].items():
            report += f"{priority}: {count}\n"

        self.notifier.send_email_notification(
            "Weekly Project Metrics",
            report
        )
