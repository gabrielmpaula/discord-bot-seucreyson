import datetime


class Time:

    @staticmethod
    def generate_created_at():
        return datetime.datetime.utcnow().isoformat()
