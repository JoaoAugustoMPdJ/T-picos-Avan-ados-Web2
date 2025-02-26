async function resolverEquacao() {
    const equacao = document.getElementById('equacao').value;
    const resultadoDiv = document.getElementById('resultado');

    if (!equacao) {
        resultadoDiv.textContent = "Por favor, insira uma equação.";
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/resolver', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ entrada: equacao }),
        });

        const data = await response.json();

        if (data.erro) {
            resultadoDiv.textContent = data.erro;
        } else {
            resultadoDiv.textContent = data.solucao;
        }
    } catch (error) {
        resultadoDiv.textContent = "Erro ao conectar com o servidor.";
    }
}