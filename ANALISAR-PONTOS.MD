💡 Observações importantes que identifiquei no código EshipTV/response.html:

1️⃣ Existe onclick duplicado no botão (erro de HTML).

onclick="javascript: addValorForm(..."
onclick="javascript: addValorForm();..."

O segundo sobrescreve o primeiro.