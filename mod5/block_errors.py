class BlockErrors:
    def __init__(self, err_types) -> None:
        self.err_types = err_types
    
    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type not in self.err_types and not any(issubclass(exc_type, i) for i in self.err_types):
            return False
        else:
            return True