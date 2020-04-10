class BoggleGame {
    constructor(secs = 60) {
        this.secs = secs; //game length
        this.showTimer();

        this.score = 0;
        this.wordList = new Set();

        this.timer = setInterval(this.tick.bind(this), 1000);

        $(".add-word").on("submit", this.handleSubmit.bind(this));
    }
    
    async handleSubmit(e) {
        e.preventDefault();
        
        const $word = $("#guess");

        let word = $word.val().toLowerCase();
        if (!word) return;

        if (this.wordList.has(word)) {
            $(".msg").html("You've already guessed this word")
            $word.val("").focus();
            return
        }

        const response = await axios.get("/check-word", { params: { word:word}});
        let validity = response.data.result

        if (validity === "ok") {
            $(".msg").html("This word is correct!");
            let newLi = $("<li>").text(word);
            $(".words").append(newLi);
            this.wordList.add(word);
            this.score += word.length;
            $("#score").text(this.score)
        } else if (validity === "not-word") {
            $(".msg").html(`${word} is not in the English lanuage`)
        } else if (validity === "not-on-board") {
            $(".msg").html(`${word} is not on the board!`)
        }
        $word.val("").focus();
    };

    /* Update timer in DOM */
    
    showTimer() {
        $(".timer").text(this.secs);
    }

    /* Tick: handle a second passing in game */

    async tick() {
        this.secs -= 1;
        this.showTimer();

        if(this.secs === 0) {
            clearInterval(this.timer)
            await this.scoreGame();
        }
    }

    async scoreGame() {
        $(".add-word").hide();
        const response = await axios.post("/score", {score: this.score});
        if(response.data.brokeRecord) {
            $(".msg").html(`You have a new highscore: ${this.score}!`)
        } else {
            $(".msg").html(`Game over! Your final score is: ${this.score}!`)
        }
    }
    
}
