document.addEventListener('DOMContentLoaded', function () {

    console.log('JavaScript do SPASB carregado com sucesso!');

    // Confirmação antes de excluir registros
    const botoesExcluir = document.querySelectorAll('.btn-excluir');

    botoesExcluir.forEach(function (botao) {

        botao.addEventListener('click', function (event) {

            const confirmacao = confirm(
                'Tem certeza que deseja excluir este registro?'
            );

            if (!confirmacao) {
                event.preventDefault();
            }

        });

    });

});