$(document).ready( function() {
    $(".alternativa").on("click", function() {
        let botao = $(this);
        let alternativa = botao.attr("class").split(" ")[3].split("-")[1];
        let questao = botao.parent().parent().attr("id").split("-")[1];
        let url = "/gabarito/marcar/" + questao + "/" + alternativa;

        $.ajax({
            url: url,
            method: 'get',
            success: function(data) {
                botao.parent().parent().parent().html(data.html);
            }
        });
    });
});