$(document).ready( function() {
    $(".correcao").on("click", function() {
        let botao = $(this);
        let correcao = botao.attr("class").split(" ")[3].split("-")[1];
        let questao = botao.parent().parent().attr("id").split("-")[1];
        let url = "/gabarito/corrigir/" + questao + "/" + correcao;

        $.ajax({
            url: url,
            method: 'get',
            success: function(data) {
                botao.parent().parent().parent().html(data.html);
            }
        });
    });
});