from hashmap.hash_map import HashMap


class BooksMap(HashMap):
    def __init__(self, size=10):
        super().__init__(size)

    #Хэш-функция
    def hash_func(self, isbn):
        clean_isbn = "".join(c for c in isbn if c.isdigit() or c == "-")
        selected = list(map(int, clean_isbn.split("-")))
        hash_value = (selected[1] << 8) + selected[2] * 31 + selected[3] % 17 + selected[4]
        return hash_value % self.size