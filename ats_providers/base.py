class ATSBase:
    def get_jobs(self):
        raise NotImplementedError

    def create_candidate(self, data):
        raise NotImplementedError

    def get_applications(self, job_id):
        raise NotImplementedError
