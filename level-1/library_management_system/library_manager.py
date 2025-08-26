from library_management_system.library import Library


class LibraryManager:
    def __init__(self, library: Library = None):
        self.library = library if library is not None else Library()
