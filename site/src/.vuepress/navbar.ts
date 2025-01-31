import { navbar } from "vuepress-theme-hope";

export default navbar([
    "/",
    {
        text: "帮助文档",
        icon: "book",
        link: "/docs/--help",
    },
    {
        text: "官方文档",
        icon: "book",
        link: "https://nuitka.net/doc/user-manual.html",
    },
]);
