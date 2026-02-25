class GmailUser:
    def __init__(self, nazwa_uzytkownika, email):
        if "@" not in email:
            raise ValueError("Email musi zawierać znak @")

        self.nazwa_uzytkownika = nazwa_uzytkownika
        self.email = email

    def __str__(self):
        return f"Użytkownik: {self.nazwa_uzytkownika}, email: {self.email}"


class Prawa:
    def __init__(self):
        self.read = False
        self.write = False

    def informacje_o_uprawnieniach(self):
        if not self.read and not self.write:
            print("Brak uprawnień: brak odczytu i pisania")
        elif self.read and self.write:
            print("Pełne uprawnienia: odczyt i pisanie")
        elif self.read:
            print("Tylko odczyt maili")
        elif self.write:
            print("Tylko pisanie maili")

    def wlacz_odczyt(self):
        self.read = True

    def wylacz_odczyt(self):
        self.read = False

    def wlacz_pisanie(self):
        self.write = True

    def wylacz_pisanie(self):
        self.write = False


class GmailAccount:
    def __init__(self, nazwa_uzytkownika, email):
        self.user = GmailUser(nazwa_uzytkownika, email)
        self.prawa = Prawa()


if __name__ == "__main__":
    try:
        konto = GmailAccount("Aldona", "aldonalemieszekgmail.com")
        konto.prawa.informacje_o_uprawnieniach()
        konto.prawa.wlacz_odczyt()
        konto.prawa.informacje_o_uprawnieniach()
    except ValueError as e:
        print("Błąd:", e)