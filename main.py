import app
import installer

from app import prnt


def main():
    installer.install()
    app.background_music()
    app.main()
    

if __name__ == "__main__":
    main()
