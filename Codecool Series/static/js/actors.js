const buttons = document.querySelectorAll("button");
const modalBody = document.querySelector(".modal-body");

buttons.forEach(button => {
    button.addEventListener("click", () => getGenres(button));
})

function getGenres(button) {
    console.log(button.id)


    fetch(`/api/actor/${button.id}/genres`)
        .then(res => res.json())
        .then(data => {
            modalBody.textContent = data.string_agg
        })
}