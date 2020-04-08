
let wordList = new Set()

$(".add-word").on("click", async function(e) {
    e.preventDefault();
    
    const $word = $("#guess");

    let word = $word.val().toLowerCase();
    if (!word) return;

    if (wordList.has(word)) {
        $(".msg").html("You've already guessed this word")
        $word.val("").focus();
        return
    }

    response = await axios.get("/check-word", { params: { word:word}});
    let validity = response.data.result

    if (validity === "ok") {
        $(".msg").html("This word is correct!");
        let newLi = $("<li>").text(word);
        $(".words").append(newLi);
        wordList.add(word);
    } else if (validity === "not-word") {
        $(".msg").html("This word is not in the English lanuage")
    } else if (validity === "not-on-board") {
        $(".msg").html("This word not on the board!")
    }
    $word.val("").focus();
});
