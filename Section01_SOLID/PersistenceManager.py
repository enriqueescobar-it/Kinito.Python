from Section01_SOLID.Journal import Journal


class PersistenceManager:

    def save_to_file(journal: Journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()
