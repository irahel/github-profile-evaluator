def get_readme(selector):
    return selector.css("article.markdown-body").get() if selector else None


def get_tags(selector):

    if not selector:
        return 0

    stacks = [
        "html",
        "css",
        "javascript",
        "jest",
        "react",
        "cypress",
        "rtl",
        "react-testing-library",
        "redux",
        "docker",
        "sql",
        "mongo",
        "node",
        "express",
        "mocha",
        "next.js",
        "typescript",
        "jwt",
        "py",
        "csharp",
        "cpp",
        "postman",
        "nginx",
        "django",
        "bash",
        "sequelize",
        "prisma",
        "bootstrap",
        "linux",
        "mac",
        "tailwind",
        "algoritmos",
        "dados",
        "redes",
        "objetos",
        "js",
    ]

    return sum(stack in selector.get().lower() for stack in stacks)
