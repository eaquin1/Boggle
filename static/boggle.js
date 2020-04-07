


$("add-word").on("click", async function(e) {
    e.preventDefault();
    const $word = $(".word");

    let word = $word.val();
    if (!word) return;
    
    response = await axios.get("/check-word", { params: { word:word}});
    console.log(response)
    });
