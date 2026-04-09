from bot.main import create_app


def main():
    app = create_app()

    print("Бот работает...")
    app.run_polling()


if __name__ == "__main__":
    main()
