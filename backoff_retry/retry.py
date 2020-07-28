from nameko import config
import backoff


class Retry:

    def __init__(self, exception):

        self.exception = exception
   
        if config.get('MAX_RETRY_TIME') is not None:
            self.max_retry_time = config.get('MAX_RETRY_TIME')
        else:
            self.max_retry_time = 1

        if config.get('MAX_RETRY') is not None:
            self.max_retries = config.get('MAX_RETRY')
        else:
            self.max_retries = 1

    def backoff_strategy(self):
        
        if self.exception is None:
            return backoff.on_exception(backoff.fibo,
                                        Exception,
                                        max_value=self.max_retry_time,
                                        max_tries=self.max_retries
                                    )
        else:
            return backoff.on_exception(backoff.fibo,
                                        self.exception,
                                        max_value=self.max_retry_time,
                                        max_tries=self.max_retries
                                    )        
