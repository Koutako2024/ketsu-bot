import ollama


def main() -> None:
    print("hoge")
    res = ollama.chat(
        model="gemma4:e2b",
        messages=[
            {
                "role": "system",
                "content": "文章中の最も効果的な自立語を「ケツ」に変換してそのまま出力してください。",
            },
            {
                "role": "user",
                "content": "ローマは1日にしてならず。",
            },
        ],
    )
    print(res.message.content)
    return


if __name__ == "__main__":
    main()
