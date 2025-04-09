from jobs.models import Job

class JobStatusManager:
    def __init__(self, job):
        self.job = job
        self.status_history = []

    def update_status(self, new_status):
        if new_status not in dict(Job.STATUS_CHOICES).keys():
            raise ValueError(f"Invalid status: {new_status}")
        self.status_history.append((self.job.status, new_status))
        self.job.status = new_status
        self.job.save()

    def get_status_history(self):
        return self.status_history