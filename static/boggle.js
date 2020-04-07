


$(".add-word").on("click", async function(e) {
    e.preventDefault();
    console.log("here")
    const $word = $("#guess");

    let word = $word.val();
    if (!word) return;

    response = await axios.get("/check-word", { params: { word:word}});
    console.log(response)
    $word.val("").focus();
});
