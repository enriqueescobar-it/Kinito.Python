from Section01_SOLID.SingleResponsivePrinciple.Journal import Journal


class PersistenceManager:
    def save_to_file(journal: Journal, filename: str):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()
