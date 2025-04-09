class JobStatusManager:
    def __init__(self, job):
        self.job = job

    def update_status(self, new_status):
        """Update the job status and return a notification message."""
        valid_statuses = ['applied', 'interview', 'offer', 'rejected']
        if new_status not in valid_statuses:
            raise ValueError("Invalid status")
        self.job.status = new_status
        self.job.save()
        return f"Status updated to {new_status} for {self.job.company} - {self.job.position}"

    def get_status_history(self):
        """Return a history of status updates (simulated)."""
        return [f"Initial: applied", f"Current: {self.job.status}"]