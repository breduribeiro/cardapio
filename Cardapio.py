import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
        img_to_bytes(img_path)
    )
    return img_html


with open("Carolina Deslandes - A Vida Toda.mp3", "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode()

st.markdown(f"""<p style='text-align: right;'>{img_to_html('el-mai-logo.jpg')}
                <p style='text-align: center;font-size:20px'><b>18/03/2023
                <br>CELEBRAÇÃO CASAMENTO CIVIL<br>ROBERTA E BRENO</b>
                <br>{img_to_html('Casamento.jpg')}
                <p><b>\"Ali, eu soube que era amor para a vida toda!<br>
                Que era contigo a minha vida toda!\"</b>
                <p style='text-align: right;'>Carolina Deslandes
                    <h1>MENU
                    <h2>Entradas
                        <p>(Todas opções serão servidas)
                    </h2>
                <p style='text-align: center;'><br><b>PASTILHA DE QUEIJO CANASTRA</b><br>
                    Servida com tomilho e mel
                <br>{img_to_html('pastilha.jpg')}
                <br><br><b>COXINHA DE RABADA</b><br>
                    Massa de abóbora fina e crocante com recheio suculento de rabada desfiada, servida com Aioli Defumado
                <br><b>{img_to_html('coxinha.jpg')}
                <br><br><b>CROQUETA DE SALMÃO</b><br>
                    Empanada com Panko, crocante por fora e muito cremosa por dentro
                <br>{img_to_html('croqueta.jpg')}
                    <h2>Pratos Principais
                        <p>(Escolha uma opção)
                    </h2>
                <p style='text-align: center;'><b>ANCHO (BASSI)</b><br>
                    Ancho, farofa crocante com castanhas, vinagrete do chef e arroz com amêndoas
                <br>{img_to_html('ancho.jpg')}
                <br><br><b>CAMARÕES À PROVENÇAL</b><br>
                    Camarões G grelhados com ervas, servidos com  arroz da panelinha do camarão
                <br>{img_to_html('camaroes.jpg')}
                <br><br><b>JARRET DE LEITÃO</b><br>
                    Cozido em baixa temperatura por 48 h, farofinha de castanhas crocantes e batata baby com ervas
                <br>{img_to_html('jarret.jpg')}
                <br><br><b>SALMÃO GRELHADO COM RISOTO DE LIMÃO SICILIANO</b><br>
                    Filet de salmão grelhado com lâminas de amêndoas e risoto de limão siciliano e açafrão.<br>Finalizado com farofinha de panceta crocante
                <br>{img_to_html('salmao.jpg')}
                <br><br><b>RISOTO DE COGUMELOS</b>
                <br>{img_to_html('risoto.jpg')}
                    <h2> Sobremesa
                        <p> (escolha uma opção)
                    </h2>
                <p style='text-align: center;'><b>LITTLE CREME BRULEE DE MATCHA</b><br>
                    Releitura do Creme Brulee em versão reduzida com matcha
                <br>{img_to_html('creme_brulee.jpg')}
                <br><br><b>PROFITEROLE</b><br>
                    Bombinha de massa francesa recheada com sorvete de creme e coberta com calda quente de chocolate belga
                <br>{img_to_html('profiterole.jpg')}
                    <h2> Bebidas
                        <p> (sirva-se à vontade)
                    </h2>
                    <p style='text-align: center;'>Drinks com Vodka
                    <br>Drinks com Gin
                    <br>Drinks com Whiskey
                    <br>Drinks Diversos
                    <br>Vinhos branco, tinto e verde
                    <br>Chopp e Cervejas
                    <br>Agua de Coco Natural
                    <br>Soda Italiana
                    <br>Suco natural jarra 500 ml
                    <br>Café Expresso
                    <br>Red Bull
                    <br>Refrigerante
                    <br>Água com gás San Pellegrino 750ml
                    <br>Água mineral Ingá sem gás
                    <br>Água mineral Ingá com gás
                    <br>Água Tônica
                    <br><br>
                    <br>A sua presença fez a nossa celebração mais feliz!<br>Gratidão!</b><br>
                    <audio controls autoplay="true">
                        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
            """,
            unsafe_allow_html=True)
