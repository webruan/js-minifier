# Índice
- [Sobre](#sobre)
- [Recursos](#recursos)
- [Estrutura de Diretórios](#estruturação)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Testes](#testes)
- [Licença](#licença)

# Sobre
O JS Minifier (nome totalmente inovador...) é o meu primeiro projeto em python que vai ser publicado, ele faz parte de uma série de "programas" que quero desemvolver para me aprofundar ainda mais nessa linguagem magnifica. 

Esse é meu método de estudos, resolver problemas em outras areas com aplicações reais. Isso me força a criar soluções que irei de fato utilizar e ainda aprendo muito com isso.

O JS Minifier é uma aplicação em fase inicial projetada para facilitar a minificação de códigos JavaScript nos meus projetos. Atualmente utilizo ferramentas de terceiros para isso, porém gostaria de algo meu, rápido e prático. Como mencionei é uma aplicação inicial, quero torna-lá capaz de minificar arquivos em massa, apenas colocando o caminho dos arquivos JS.

O processo de minificação de código é essencial para reduzir o tamanho dos arquivos JavaScript, tornando-os mais eficientes em termos de carregamento em aplicações web.

Esse app fornece uma interface simples para inserir o código JavaScript e obter uma versão minificada do mesmo. 

Atualmente oferece recursos simples como:
 - Remoção de comentários
 - Remoção de espaços em branco desnecessários
 - Remoção de "enters"/novas linhas

Estou ansioso para receber feedbacks e aprimorar continuamente essa ferramenta. Sua contribuição e suas sugestões são valiosas para mim.

# Referências e Recursos de Aprendizado
Aqui estão alguns links que foram valiosos durante o desenvolvimento do JS Minifier, fornecendo soluções e insights para o desenvolvimento do código e da interface, assim como auxiliando no meu aprendizado em Python.

- [Stack Overflow: TypeError - missing 1 required positional argument: 'index1'](https://stackoverflow.com/questions/63525858/typeerror-get-missing-1-required-positional-argument-index1)
  - Esta discussão ajudou a resolver um erro relacionado a argumentos ausentes em uma função.

- [Stack Overflow: Python - Obtenha o tamanho de uma string em bytes](https://stackoverflow.com/questions/30686701/python-get-size-of-string-in-bytes)
  - Aqui, aprendi como calcular o tamanho de uma string em bytes, o que foi útil para calcular o tamanho do código e calcular a economia de armazenamento.

- [GeeksforGeeks: PyQt5 - Como limpar o conteúdo de uma QLabel (clear e setText)](https://www.geeksforgeeks.org/pyqt5-how-to-clear-the-content-of-label-clear-and-settext-method/)
  - Este tutorial explicou como definir o conteúdo de uma QLabel através de uma funções, o que foi útil para mostrar o tamanho do código na interface.

- [Stack Overflow: Desabilitar ou bloquear o QTextEdit no PyQt](https://stackoverflow.com/questions/23696878/disable-or-lock-text-edit-pyqt)
  - Esta discussão forneceu informações sobre como desabilitar um QTextEdit, que era necessário para a saída de código não ser editável e ficar visualmente mais intuitivo ao usuário.

- [Stack Overflow: Adicionar texto ao QPlainTextEdit no PyQt](https://stackoverflow.com/questions/9841820/add-text-to-qplaintextedit-in-pyqt-the-result-is-a-status-log)
  - Aprender como adicionar texto a um QPlainTextEdit através de uma função foi fundamental para exibir o código minificado.

- [LearnDataAnalysis.org: Implementação de cópia de conteúdo para a área de transferência no PyQt5](https://learndataanalysis.org/source-code-implement-copy-content-to-clipboard-feature-pyqt5-tutorial/)
  - Este tutorial me guiou na implementação da funcionalidade de copiar o código para a área de transferência.

- [Python-Commandments.org: PyQt - Como definir um ícone de janela com PyQt5](https://python-commandments.org/pyqt-icon/)
  - Aqui, aprendi como definir um ícone para na janela do aplicativo, o que adiciona um toque visual mais "profissional".

- [Stack Overflow: Como definir um ícone de janela com PyQt5](https://stackoverflow.com/questions/42602713/how-to-set-a-window-icon-with-pyqt5)
  - Essa discução me auxiliou a como definir o ícone quando a imagem está em outro diretório.

Esses recursos foram fundamentais para o desenvolvimento bem-sucedido do JS Minifier até o momento.

# Estruturação de diretórios
```
js_minifier/
├── assets/
│ ├── images/
│ │ └── javascript-logo.svg
│ └── styles/
│ └── style.qss
├── interface/
│ ├── __init__.py
│ ├── main.py
│ ├── buttons.py
│ └── textbox.py
├── functions/
│ ├── __init__.py
│ ├── clear.py
│ ├── copy.py
│ └── remove.py
├── main.py
└── README.md
```

# Como usar
A interface do JS Minifier é projetada para ser simples e intuitiva. Com apenas dois passos, você pode minificar seu código JavaScript. Aqui estão as funcionalidades e como usá-las:

### 1. Inserindo o código

**``Código de entrada:``** Este é o campo de texto onde você deve colar seu código JavaScript. Insira seu código e o JS Minifier fará o resto.

### 2. Minificando o código

**``Remover espaços:``** Clique no botão "Remover espaços" para iniciar o processo de minificação. O JS Minifier irá remover comentários e espaços em branco desnecessários, tornando seu código mais compacto e eficiente.

### 3. Visualizando o resultado

**``Código de saída:``** Após a minificação, o código minificado aparecerá automaticamente neste campo. Observe que este campo não é habilitado para edição, pois exibe apenas o resultado da minificação.

### 4. Copiando o código minificado

**``Copiar código:``** Para usar o código minificado, clique no botão "Copiar código". Isso copiará o código minificado para a área de transferência do seu sistema, pronto para ser colado em seu projeto.

### 5. Limpar campos

**``Limpar campos:``** Se você deseja recomeçar ou trabalhar com um novo código, basta clicar em "Limpar campos". Isso apagará todo o conteúdo nos campos de entrada e saída.

[Interface](./assets/images/app.png)

# Testes
Executei alguns testes para calcular a economia de armazenamento entre o códio de entrada e saída e também a limitação do minifier.
* Método de carregamento dos scripts: ```async```
* Página vazia apenas com a tag ```<script src="">``` utilizadas no ```<body>```
* Método de carreamento da página: ```CTRL + F5```

## Primeiro teste
- *O funcionamento continuo após a minificação:* **Sim**

### Armazenamento
- *Código de entrada:* **0.9 Bytes**
- *Código de saída:* **0.54 Bytes**

> *Economia de 0.36 Bytes*

### Solicitação/resposta
- *Tempo médio de download (**minificado**):* <sub>(2.92 + 3.95 + 3.81 + 4.27) / 4</sub> = **3.73 ms**
- *Tempo médio de download (**normal**):* <sub>(7.78 + 4.13 + 5.88 + 4.37) / 4</sub> = **5.79 ms**

**Diferença de tempo entre cada teste (*minificado - normal*):**

1. *Primeiro teste:* <sub>2.92 ms - 7.78 ms</sub> = **-4.86 ms** (minificado mais rápido)
2. *Segundo teste:* <sub>3.95 ms - 4.13 ms</sub> = **-0.18 ms** (minificado mais rápido)
3. *Terceiro teste:* <sub>3.81 ms - 5.88 ms</sub> = **-2.07 ms** (minificado mais rápido)
4. *Quarto teste:* <sub>4.27 ms - 4.37 ms</sub> = **-0.10 ms** (minificado mais rápido)

> *Média aproximada de **2.05 ms** a favor do código minificado.*

### Código de entrada
```javascript
const questions = document.querySelectorAll('.column_benefits p');
const answers = document.querySelectorAll('.row.down.answer');

function showAnswer(index) {
  // Remove a classe "selected" de todas as perguntas
  questions.forEach(question => {
    question.classList.remove('selected');
  });

  // Adiciona a classe "selected" à pergunta atual
  questions[index].classList.add('selected');

  // Oculta a resposta anterior (se houver alguma)
  const previousAnswer = document.querySelector('.row.down.selected');
  if (previousAnswer) {
    previousAnswer.classList.remove('selected');
  }

  // Mostra a resposta correspondente
  answers[index].classList.add('selected');
}

// Adiciona um ouvinte de eventos para cada pergunta
questions.forEach((question, index) => {
  question.addEventListener('click', () => {
    showAnswer(index);
  });
});

// Mostra a resposta inicial (a primeira pergunta)
showAnswer(0);
```

### Código de saída
```javascript
const questions=document.querySelectorAll('.column_benefits p'); const answers=document.querySelectorAll('.row.down.answer');function showAnswer(index){questions.forEach(question=>{question.classList.remove('selected');});questions[index].classList.add('selected'); const previousAnswer=document.querySelector('.row.down.selected');if(previousAnswer){previousAnswer.classList.remove('selected');}answers[index].classList.add('selected');}questions.forEach((question,index)=>{question.addEventListener('click',()=>{showAnswer(index);});});showAnswer(0);
```

## Segundo teste
- *O funcionamento continuo após a minificação:* **Sim**

### Armazenamento
- *Código de entrada =* **5.46 KB**
- *Código de saída =* **2.67 KB**

> *Economia de 2.79 KB*

### Solicitação/resposta
- *Tempo médio de download (**minificado**):* <sub>(15.57 + 19.56 + 6.47 + 9.79) / 4</sub> = **12.09 ms**
- *Tempo médio de download (**normal**):* <sub>(15.74 + 26.53 + 6.69 + 11.62) / 4</sub> = **15.39 ms**

**Diferença de tempo entre cada teste (*minificado - normal*):**

1. *Primeiro teste:* <sub>15.57 ms - 15.74 ms</sub> = **-0.17 ms** (minificado mais rápido)
2. *Segundo teste:* <sub>19.56 ms- 26.53 ms</sub> = **-6.97 ms** (minificado mais rápido)
3. *Terceiro teste:* <sub>6.47 ms - 6.69 ms</sub> = **-0.22 ms** (minificado mais rápido)
4. *Quarto teste:* <sub>9.79 ms - 11.62 ms </sub> = **-1.83 ms** (minificado mais rápido)

> *Média aproximada de **3.29 ms** a favor do código minificado.*

### Código de entrada
```javascript
  const column1 = document.getElementById('column-01');
  const column2 = document.getElementById('column-02');
  const rowHeight = 102; // Defina a altura de cada linha (row) para ajustar o deslocamento
  const slideInterval = 4000; // Defina o intervalo de tempo entre os slides (em milissegundos)

  // Função para gerar um elemento de linha (row) com base no texto e ID da imagem
  function createRowElement(text, imageId) {
    const row = document.createElement('div');
    row.classList.add('row');

    const imgDiv = document.createElement('div');
    imgDiv.classList.add('img');
    imgDiv.id = imageId;

    const pElement = document.createElement('p');
    pElement.textContent = text;

    row.appendChild(imgDiv);
    row.appendChild(pElement);

    return row;
  }

  // Função para mover os itens para baixo e reaparecer no topo
  function slideItemsUp(column1) {
    const rows = column1.querySelectorAll('.row');

    // Adiciona a classe fade-out aos elementos que estão saindo do topo
    rows[0].classList.add('fade-out');

    // Move os itens para baixo
    column1.style.transition = 'transform 2s ease-in';
    column1.style.transform = `translateY(-${rowHeight}px)`;

    // Aguarda um curto intervalo para que a transição termine
    setTimeout(() => {
      // Remove a classe fade-out e o elemento do topo da coluna
      rows[0].classList.remove('fade-out');
      rows[0].remove();

      // Remove a transição para que possamos reposicionar os itens sem animação
      column1.style.transition = 'none';

      // Move o primeiro item para o final da coluna
      const firstRow = rows[0];
      column1.appendChild(firstRow.cloneNode(true));
      firstRow.remove();

      // Adiciona a classe fade-in ao novo item recém-adicionado
      const newRow = column1.lastElementChild;
      newRow.classList.add('fade-in');

      // Reposiciona a coluna para a posição original (sem o translateY)
      column1.style.transform = 'translateY(0)';

      // Remove a classe fade-in após um curto período de tempo para a animação ser repetida
      setTimeout(() => {
        newRow.classList.remove('fade-in');
      }, 1000); // Tempo da animação em milissegundos
    }, 1000);
  }

  // Função para mover os itens para baixo e reaparecer no topo
  function slideItemsDown(column2) {
    const rows = column2.querySelectorAll('.row');

    // Adiciona a classe fade-out aos elementos que estão saindo do topo
    rows[3].classList.add('fade-out');

    // Move os itens para baixo
    column2.style.transition = 'transform 2s ease-in';
    column2.style.transform = `translateY(${rowHeight}px)`;

    // Aguarda um curto intervalo para que a transição termine
    setTimeout(() => {
      // Remove a classe fade-out e o elemento do topo da coluna
      rows[3].classList.remove('fade-out');
      rows[3].remove();

      // Remove a transição para que possamos reposicionar os itens sem animação
      column2.style.transition = 'none';

      // Move o primeiro item para o final da coluna
      const firstRow = rows[3];
      column2.appendChild(firstRow.cloneNode(true));
      firstRow.remove();

      // Adiciona a classe fade-in ao novo item recém-adicionado
      const newRow = column2.firstElementChild;
      newRow.classList.add('fade-in');

      // Reposiciona a coluna para a posição original (sem o translateY)
      column2.style.transform = 'translateY(0)';

      // Remove a classe fade-in após um curto período de tempo para a animação ser repetida
      setTimeout(() => {
        newRow.classList.remove('fade-in');
      }, 1000); // Tempo da animação em milissegundos
    }, 1000);
  }

  // Função para iniciar o slider
  function startSliderUp(column1) {
    // Gera os elementos iniciais da coluna utilizando os elementos já presentes no HTML
    const rows = column1.querySelectorAll('.row');
    rows.forEach(row => {
      const text = row.querySelector('p').textContent;
      const imageId = row.querySelector('.img').id;
      const newRow = createRowElement(text, imageId);
      column1.appendChild(newRow);
      row.remove();
    });

    // Chama a função para mover os itens a cada intervalo de tempo definido
    setInterval(() => slideItemsUp(column1), slideInterval);
  }

  // Função para iniciar o slider
  function startSliderDown(column2) {
    // Gera os elementos iniciais da coluna utilizando os elementos já presentes no HTML
    const rows = column2.querySelectorAll('.row');
    rows.forEach(row => {
      const text = row.querySelector('p').textContent;
      const imageId = row.querySelector('.img').id;
      const newRow = createRowElement(text, imageId);
      column2.appendChild(newRow);
      row.remove();
    });

    // Chama a função para mover os itens a cada intervalo de tempo definido
    setInterval(() => slideItemsDown(column2), slideInterval);
  }
  // Utilitário para verificar se um elemento está visível no viewport
  function isVisible(element) {
    const bounding = element.getBoundingClientRect();
    return (
      bounding.top >= 0 &&
      bounding.left >= 0 &&
      bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  // Função para iniciar o slider quando as colunas estiverem visíveis
  function initSliderWhenVisible() {
    if (isVisible(column1)) {
      startSliderUp(column1);
      startSliderDown(column2);
    }
  }

  startSliderUp(column1);
  startSliderDown(column2);
```

### Código de saída
```javascript
  const column1=document.getElementById('column-01'); const column2=document.getElementById('column-02'); const rowHeight=102; const slideInterval=4000;function createRowElement(text,imageId){ const row=document.createElement('div');row.classList.add('row'); const imgDiv=document.createElement('div');imgDiv.classList.add('img');imgDiv.id=imageId; const pElement=document.createElement('p');pElement.textContent=text;row.appendChild(imgDiv);row.appendChild(pElement);return row;}function slideItemsUp(column1){ const rows=column1.querySelectorAll('.row');rows[0].classList.add('fade-out');column1.style.transition='transform 2s ease-in';column1.style.transform=`translateY(-${rowHeight}px)`;setTimeout(()=>{rows[0].classList.remove('fade-out');rows[0].remove();column1.style.transition='none'; const firstRow=rows[0];column1.appendChild(firstRow.cloneNode(true));firstRow.remove(); const newRow=column1.lastElementChild;newRow.classList.add('fade-in');column1.style.transform='translateY(0)';setTimeout(()=>{newRow.classList.remove('fade-in');},1000);},1000);}function slideItemsDown(column2){ const rows=column2.querySelectorAll('.row');rows[3].classList.add('fade-out');column2.style.transition='transform 2s ease-in';column2.style.transform=`translateY(${rowHeight}px)`;setTimeout(()=>{rows[3].classList.remove('fade-out');rows[3].remove();column2.style.transition='none'; const firstRow=rows[3];column2.appendChild(firstRow.cloneNode(true));firstRow.remove(); const newRow=column2.firstElementChild;newRow.classList.add('fade-in');column2.style.transform='translateY(0)';setTimeout(()=>{newRow.classList.remove('fade-in');},1000);},1000);}function startSliderUp(column1){ const rows=column1.querySelectorAll('.row');rows.forEach(row=>{ const text=row.querySelector('p').textContent; const imageId=row.querySelector('.img').id; const newRow=createRowElement(text,imageId);column1.appendChild(newRow);row.remove();});setInterval(()=>slideItemsUp(column1),slideInterval);}function startSliderDown(column2){ const rows=column2.querySelectorAll('.row');rows.forEach(row=>{ const text=row.querySelector('p').textContent; const imageId=row.querySelector('.img').id; const newRow=createRowElement(text,imageId);column2.appendChild(newRow);row.remove();});setInterval(()=>slideItemsDown(column2),slideInterval);}function isVisible(element){ const bounding=element.getBoundingClientRect();return (bounding.top>=0&&bounding.left>=0&&bounding.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&bounding.right<=(window.innerWidth||document.documentElement.clientWidth));}function initSliderWhenVisible(){if(isVisible(column1)){startSliderUp(column1);startSliderDown(column2);}}startSliderUp(column1);startSliderDown(column2);
```

## Terceiro teste
- *O funcionamento continuo após a minificação:* **Sim**

### Armazenamento
- *Código de entrada =* **10.66 KB**
- *Código de saída =* **8.1 KB**

> *Economia de 2.56 KB*

### Solicitação/resposta
- *Tempo médio de download (**minificado**):* <sub> (7.16 + 4.56 + 5.28 + 3.39) / 4</sub> = **5.59 ms**
- *Tempo médio de download (**normal**):* <sub>(7.18 + 6.02 + 5.36 + 4.89) / 4</sub> = **5.86 ms**

**Diferença de tempo entre cada teste (*minificado - normal*):**

1. *Primeiro teste:* <sub>7.16 ms - 7.18 ms</sub> = **-0.02 ms** (minificado mais rápido)
2. *Segundo teste:* <sub>4.56 ms - 6.02 ms</sub> = **-1.46 ms** (minificado mais rápido)
3. *Terceiro teste:* <sub>5.28 ms - 5.36 ms</sub> = **-0.08 ms** (minificado mais rápido)
4. *Quarto teste:* <sub>3.39 ms - 4.89 ms </sub> = **-1.5 ms** (minificado mais rápido)

> *Média aproximada de **0.26 ms** a favor do código minificado.*

### Código de entrada
```javascript
// Dados utilizados na simulação
const dataImovel = [
  ["Crédito","Parcelas","Plano"],["R$ 70.000,00","R$ 345,00","200X"],["R$ 75.000,00","R$ 369,00","200X"],["R$ 80.000,00","R$ 394,00","200X"],["R$ 85.000,00","R$ 419,00","200X"],["R$ 90.000,00","R$ 443,00","200X"],["R$ 95.000,00","R$ 468,00","200X"],["R$ 100.000,00","R$ 493,00","200X"],["R$ 105.000,00","R$ 517,00","200X"],["R$ 110.000,00","R$ 542,00","200X"],["R$ 115.000,00","R$ 567,00","200X"],["R$ 120.000,00","R$ 591,00","200X"],["R$ 125.000,00","R$ 616,00","200X"],["R$ 130.000,00","R$ 641,00","200X"],["R$ 135.000,00","R$ 665,00","200X"],["R$ 140.000,00","R$ 679,00","200X"],["R$ 150.000,00","R$ 727,00","200X"],["R$ 160.000,00","R$ 776,00","200X"],["R$ 170.000,00","R$ 824,00","200X"],["R$ 180.000,00","R$ 873,00","200X"],["R$ 190.000,00","R$ 921,00","200X"],["R$ 200.000,00","R$ 970,00","200X"],["R$ 210.000,00","R$ 1.018,00","200X"],["R$ 220.000,00","R$ 1.067,00","200X"],["R$ 230.000,00","R$ 1.115,00","200X"],["R$ 240.000,00","R$ 1.164,00","200X"],["R$ 250.000,00","R$ 1.212,00","200X"],["R$ 260.000,00","R$ 1.261,00","200X"],["R$ 270.000,00","R$ 1.309,00","200X"],["R$ 280.000,00","R$ 1.335,00","200X"],["R$ 290.000,00","R$ 1.383,00","200X"],["R$ 300.000,00","R$ 1.431,00","200X"],["R$ 310.000,00","R$ 1.478,00","200X"],["R$ 320.000,00","R$ 1.526,00","200X"],["R$ 330.000,00","R$ 1.574,00","200X"],["R$ 340.000,00","R$ 1.621,00","200X"],["R$ 350.000,00","R$ 1.669,00","200X"],["R$ 360.000,00","R$ 1.717,00","200X"],["R$ 370.000,00","R$ 1.765,00","200X"],["R$ 380.000,00","R$ 1.812,00","200X"],["R$ 390.000,00","R$ 1.860,00","200X"],["R$ 400.000,00","R$ 1.908,00","200X"],["R$ 410.000,00","R$ 1.955,00","200X"],["R$ 420.000,00","R$ 2.003,00","200X"],["R$ 430.000,00","R$ 2.051,00","200X"],["R$ 440.000,00","R$ 2.099,00","200X"],["R$ 450.000,00","R$ 2.146,00","200X"],["R$ 460.000,00","R$ 2.194,00","200X"],["R$ 470.000,00","R$ 2.242,00","200X"],["R$ 480.000,00","R$ 2.289,00","200X"],["R$ 490.000,00","R$ 2.337,00","200X"],["R$ 500.000,00","R$ 2.385,00","200X"],["R$ 510.000,00","R$ 2.432,00","200X"],["R$ 520.000,00","R$ 2.480,00","200X"],["R$ 530.000,00","R$ 2.528,00","200X"],["R$ 540.000,00","R$ 2.576,00","200X"],["R$ 550.000,00","R$ 2.623,00","200X"],["R$ 560.000,00","R$ 2.671,00","200X"],["R$ 600.000,00","R$ 2.825,00","200X"],["R$ 650.000,00","R$ 3.061,00","200X"],["R$ 700.000,00","R$ 3.296,00","200X"],["R$ 750.000,00","R$ 3.532,00","200X"],["R$ 800.000,00","R$ 3.767,00","200X"],["R$ 850.000,00","R$ 4.003,00","200X"],["R$ 900.000,00","R$ 4.238,00","200X"]
]

const dataAuto = [
  ["Crédito", "Parcelas", "Plano"], ["R$ 25.000,00", "R$ 484,00", "50x"], ["R$ 27.500,00", "R$ 532,00", "50x"], ["R$ 30.000,00", "R$ 581,00", "50x"], ["R$ 32.500,00", "R$ 629,00", "50x"], ["R$ 35.000,00", "R$ 678,00", "50x"], ["R$ 37.500,00", "R$ 726,00", "50x"], ["R$ 40.000,00", "R$ 774,00", "50x"], ["R$ 42.500,00", "R$ 823,00", "50x"], ["R$ 45.000,00", "R$ 871,00", "50x"], ["R$ 47.500,00", "R$ 920,00", "50x"], ["R$ 50.000,00", "R$ 679,00", "72x"], ["R$ 52.500,00", "R$ 713,00", "72x"], ["R$ 55.000,00", "R$ 746,00", "72x"], ["R$ 57.500,00", "R$ 780,00", "72x"], ["R$ 60.000,00", "R$ 814,00", "72x"], ["R$ 62.500,00", "R$ 848,00", "72x"], ["R$ 65.000,00", "R$ 882,00", "72x"], ["R$ 67.500,00", "R$ 813,00", "80x"], ["R$ 72.500,00", "R$ 874,00", "80x"], ["R$ 77.500,00", "R$ 934,00", "80x"], ["R$ 82.500,00", "R$ 994,00", "80x"], ["R$ 87.500,00", "R$ 1.055,00", "80x"], ["R$ 92.500,00", "R$ 1.115,00", "80x"], ["R$ 97.500,00", "R$ 1.175,00", "80x"], ["R$ 102.500,00", "R$ 1.235,00", "80x"], ["R$ 107.500,00", "R$ 1.296,00", "80x"], ["R$ 112.500,00", "R$ 1.356,00", "80x"], ["R$ 117.500,00", "R$ 1.416,00", "80x"], ["R$ 122.500,00", "R$ 1.477,00", "80x"], ["R$ 125.000,00", "R$ 1.507,00", "90x"], ["R$ 125.000,00", "R$ 1.333,00", "90x"], ["R$ 130.000,00", "R$ 1.387,00", "90x"], ["R$ 140.000,00", "R$ 1.493,00", "90x"], ["R$ 150.000,00", "R$ 1.600,00", "90x"], ["R$ 160.000,00", "R$ 1.707,00", "90x"], ["R$ 170.000,00", "R$ 1.814,00", "90x"], ["R$ 180.000,00", "R$ 1.920,00", "90x"], ["R$ 190.000,00", "R$ 2.027,00", "90x"], ["R$ 200.000,00", "R$ 2.134,00", "90x"]
]

// Elementos do DOM
const btnType = document.querySelectorAll('.type_selector');
const valueText = document.getElementById('value');
const valueResult = document.getElementById('result_value');
const valueResultDesc = document.getElementById('result_value_desc');
const btnAdd = document.getElementById('add');
const btnSubtract = document.getElementById('sub');
const btnTotal = document.getElementById('total');
const btnPortion = document.getElementById('portion'); 
const btnSimulate = document.getElementById('simulate');
const cSimulationResult = document.getElementById('c_result_value');
const fSimulationResult = document.getElementById('f_result_value');
const cSimulationQuota = document.getElementById('c_quota_x');
const fSimulationQuota = document.getElementById('f_quota_x');
const cSimulationQuotaValue = document.getElementById('c_quota_value');
const fSimulationQuotaValue = document.getElementById('f_quota_value');
const economyValue = document.getElementById('economy');


// Aumenta e diminui o valor que aparece no display de crédito
let currentCreditIndex = 1;
// Define o tipo inicialmente como imóvel
let currentType = dataImovel;
// Define o tipo de simulação inicialmente como "total"
let currentSimulationType = 'total';

function updateCreditValue() {
  const credit = currentType[currentCreditIndex][0];
  const quota = currentType[currentCreditIndex][1];
  valueText.textContent = currentSimulationType === 'total' ? credit : quota;
}

function handleAddClick() {
  if (currentCreditIndex < currentType.length - 1) {
    currentCreditIndex++;
    updateCreditValue();
  }
}

function handleSubtractClick() {
  if (currentCreditIndex > 1) {
    currentCreditIndex--;
    updateCreditValue();
  }
}

// Função para simular o valor
btnSimulate.addEventListener('click', () => {
  simulateLoan(currentType);
});

function simulateLoan(currentType) {
  document.getElementById('loading').classList.add('loading');
  document.getElementById('spinner').classList.add('spinner');
  setTimeout(() => {
    const creditValue = valueText.textContent;
    const credit = currentType[currentCreditIndex][0];
    const quotaValue = currentType[currentCreditIndex][1];
    const planValue = currentType[currentCreditIndex][2];

    // Atualize o elemento de resultado com o valor simulado
    valueResult.textContent = creditValue;
    cSimulationResult.textContent = creditValue;
    cSimulationQuota.textContent = planValue.toLowerCase() + ' de';
    cSimulationQuotaValue.textContent = quotaValue;
    fSimulationQuotaValue.textContent = quotaValue;
    valueResultDesc.textContent = '(valor total)';

    if (planValue.toLowerCase() === '50x') {
      fSimulationQuota.textContent = '100x de';
    }

    if (planValue.toLowerCase() === '200x') {
      fSimulationQuota.textContent = '300x de';
    } 

    function formatCurrency(value) {
      return value.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL',
        minimumFractionDigits: 2,
      });
    }

    // Obtém o valor da parcela do plano e adiciona 2
    const quotaNum = parseFloat(quotaValue.replace(/[^0-9,.]/g, '').replace(',', '.')); // Remove caracteres não numéricos e substitui vírgula por ponto
    const planNum = parseFloat(fSimulationQuota.textContent.replace(/[^0-9,.]/g, '').replace(',', '.')); // Remove caracteres não numéricos e substitui vírgula por ponto
    const simulationResultValue = Math.round(planNum * quotaNum * 100); // Multiplica por 100 para obter o valor em centavos e arredonda

    // Formata o valor da parcela simulada como "R$00.000,00"
    fSimulationResult.textContent = formatCurrency(simulationResultValue / 100); // Divide por 100 para obter o valor em reais novamente

    // Calcular diferença entre o valor simulado e o valor do crédito total
    const creditToNum = parseInt(creditValue.replace(/[^0-9]/g, '').replace(',', '.')); // Remove caracteres não numéricos e substitui vírgula por ponto
    const differenceValue = Math.round((simulationResultValue - creditToNum)); // Multiplica o crédito total por 100 para obter o valor em centavos e arredonda

    // Exibir a diferença como economia
    economyValue.textContent = formatCurrency(differenceValue / 100); // Divide por 100 para obter o valor em reais novamente

    if (currentSimulationType !== 'total') {
      valueResultDesc.textContent = '(valor da parcela)';
      cSimulationResult.textContent = credit;
    }

    // Remover a classe "loading" após um pequeno atraso para que o efeito seja perceptível
    document.getElementById('loading').classList.remove('loading');
    document.getElementById('spinner').classList.remove('spinner');
  }, 500); // 500ms (meio segundo)
}

// Event listener para o botão de Crédito total
btnTotal.addEventListener('click', () => {
  if (currentSimulationType !== 'total') {
    currentSimulationType = 'total';
    btnTotal.classList.add('selected'); // Adiciona a classe "selected" no botão "Crédito total"
    btnPortion.classList.remove('selected'); // Remove a classe "selected" do botão "Valor da parcela"
    updateCreditValue();
  }
});

// Event listener para o botão de Valor da parcela
btnPortion.addEventListener('click', () => {
  if (currentSimulationType !== 'portion') {
    currentSimulationType = 'portion';
    btnTotal.classList.remove('selected'); // Remove a classe "selected" do botão "Crédito total"
    btnPortion.classList.add('selected'); // Adiciona a classe "selected" no botão "Valor da parcela"
    updateCreditValue();
  }
});

// Event listeners para os botões de aumentar e diminuir o crédito
btnAdd.addEventListener('click', handleAddClick);
btnSubtract.addEventListener('click', handleSubtractClick);

// Atualizar o valor do crédito inicialmente
updateCreditValue();

const houseBtn = document.getElementById('houseBtn');
const carBtn = document.getElementById('carBtn');

// Função para alternar entre os botões e carregar os dados corretos
function handleTypeClick(event) {
  const clickedBtn = event.currentTarget;

  if (clickedBtn.classList.contains('active')) {
    return;
  }

  document.querySelector('.type_selector.active').classList.remove('active');
  clickedBtn.classList.add('active');

  if (clickedBtn === houseBtn) {
    currentType = dataImovel;
  } else if (clickedBtn === carBtn) {
    currentType = dataAuto;
  }

  currentCreditIndex = 1;

  // Atualize os elementos com os dados apropriados com base no tipo selecionado
  updateCreditValue();
}

// Adiciona o ouvinte de evento a cada botão
btnType.forEach(btn => {
  btn.addEventListener('click', handleTypeClick);
});

// Chamada inicial para carregar os dados de imóvel (caso queira que o imóvel seja selecionado inicialmente)
handleTypeClick({ currentTarget: houseBtn });
```

### Código de saída
```javascript
 const dataImovel=[["Crédito","Parcelas","Plano"],["R$ 70.000,00","R$ 345,00","200X"],["R$ 75.000,00","R$ 369,00","200X"],["R$ 80.000,00","R$ 394,00","200X"],["R$ 85.000,00","R$ 419,00","200X"],["R$ 90.000,00","R$ 443,00","200X"],["R$ 95.000,00","R$ 468,00","200X"],["R$ 100.000,00","R$ 493,00","200X"],["R$ 105.000,00","R$ 517,00","200X"],["R$ 110.000,00","R$ 542,00","200X"],["R$ 115.000,00","R$ 567,00","200X"],["R$ 120.000,00","R$ 591,00","200X"],["R$ 125.000,00","R$ 616,00","200X"],["R$ 130.000,00","R$ 641,00","200X"],["R$ 135.000,00","R$ 665,00","200X"],["R$ 140.000,00","R$ 679,00","200X"],["R$ 150.000,00","R$ 727,00","200X"],["R$ 160.000,00","R$ 776,00","200X"],["R$ 170.000,00","R$ 824,00","200X"],["R$ 180.000,00","R$ 873,00","200X"],["R$ 190.000,00","R$ 921,00","200X"],["R$ 200.000,00","R$ 970,00","200X"],["R$ 210.000,00","R$ 1.018,00","200X"],["R$ 220.000,00","R$ 1.067,00","200X"],["R$ 230.000,00","R$ 1.115,00","200X"],["R$ 240.000,00","R$ 1.164,00","200X"],["R$ 250.000,00","R$ 1.212,00","200X"],["R$ 260.000,00","R$ 1.261,00","200X"],["R$ 270.000,00","R$ 1.309,00","200X"],["R$ 280.000,00","R$ 1.335,00","200X"],["R$ 290.000,00","R$ 1.383,00","200X"],["R$ 300.000,00","R$ 1.431,00","200X"],["R$ 310.000,00","R$ 1.478,00","200X"],["R$ 320.000,00","R$ 1.526,00","200X"],["R$ 330.000,00","R$ 1.574,00","200X"],["R$ 340.000,00","R$ 1.621,00","200X"],["R$ 350.000,00","R$ 1.669,00","200X"],["R$ 360.000,00","R$ 1.717,00","200X"],["R$ 370.000,00","R$ 1.765,00","200X"],["R$ 380.000,00","R$ 1.812,00","200X"],["R$ 390.000,00","R$ 1.860,00","200X"],["R$ 400.000,00","R$ 1.908,00","200X"],["R$ 410.000,00","R$ 1.955,00","200X"],["R$ 420.000,00","R$ 2.003,00","200X"],["R$ 430.000,00","R$ 2.051,00","200X"],["R$ 440.000,00","R$ 2.099,00","200X"],["R$ 450.000,00","R$ 2.146,00","200X"],["R$ 460.000,00","R$ 2.194,00","200X"],["R$ 470.000,00","R$ 2.242,00","200X"],["R$ 480.000,00","R$ 2.289,00","200X"],["R$ 490.000,00","R$ 2.337,00","200X"],["R$ 500.000,00","R$ 2.385,00","200X"],["R$ 510.000,00","R$ 2.432,00","200X"],["R$ 520.000,00","R$ 2.480,00","200X"],["R$ 530.000,00","R$ 2.528,00","200X"],["R$ 540.000,00","R$ 2.576,00","200X"],["R$ 550.000,00","R$ 2.623,00","200X"],["R$ 560.000,00","R$ 2.671,00","200X"],["R$ 600.000,00","R$ 2.825,00","200X"],["R$ 650.000,00","R$ 3.061,00","200X"],["R$ 700.000,00","R$ 3.296,00","200X"],["R$ 750.000,00","R$ 3.532,00","200X"],["R$ 800.000,00","R$ 3.767,00","200X"],["R$ 850.000,00","R$ 4.003,00","200X"],["R$ 900.000,00","R$ 4.238,00","200X"]] 
 const dataAuto=[["Crédito","Parcelas","Plano"],["R$ 25.000,00","R$ 484,00","50x"],["R$ 27.500,00","R$ 532,00","50x"],["R$ 30.000,00","R$ 581,00","50x"],["R$ 32.500,00","R$ 629,00","50x"],["R$ 35.000,00","R$ 678,00","50x"],["R$ 37.500,00","R$ 726,00","50x"],["R$ 40.000,00","R$ 774,00","50x"],["R$ 42.500,00","R$ 823,00","50x"],["R$ 45.000,00","R$ 871,00","50x"],["R$ 47.500,00","R$ 920,00","50x"],["R$ 50.000,00","R$ 679,00","72x"],["R$ 52.500,00","R$ 713,00","72x"],["R$ 55.000,00","R$ 746,00","72x"],["R$ 57.500,00","R$ 780,00","72x"],["R$ 60.000,00","R$ 814,00","72x"],["R$ 62.500,00","R$ 848,00","72x"],["R$ 65.000,00","R$ 882,00","72x"],["R$ 67.500,00","R$ 813,00","80x"],["R$ 72.500,00","R$ 874,00","80x"],["R$ 77.500,00","R$ 934,00","80x"],["R$ 82.500,00","R$ 994,00","80x"],["R$ 87.500,00","R$ 1.055,00","80x"],["R$ 92.500,00","R$ 1.115,00","80x"],["R$ 97.500,00","R$ 1.175,00","80x"],["R$ 102.500,00","R$ 1.235,00","80x"],["R$ 107.500,00","R$ 1.296,00","80x"],["R$ 112.500,00","R$ 1.356,00","80x"],["R$ 117.500,00","R$ 1.416,00","80x"],["R$ 122.500,00","R$ 1.477,00","80x"],["R$ 125.000,00","R$ 1.507,00","90x"],["R$ 125.000,00","R$ 1.333,00","90x"],["R$ 130.000,00","R$ 1.387,00","90x"],["R$ 140.000,00","R$ 1.493,00","90x"],["R$ 150.000,00","R$ 1.600,00","90x"],["R$ 160.000,00","R$ 1.707,00","90x"],["R$ 170.000,00","R$ 1.814,00","90x"],["R$ 180.000,00","R$ 1.920,00","90x"],["R$ 190.000,00","R$ 2.027,00","90x"],["R$ 200.000,00","R$ 2.134,00","90x"]] 
 const btnType=document.querySelectorAll('.type_selector'); const valueText=document.getElementById('value'); const valueResult=document.getElementById('result_value'); const valueResultDesc=document.getElementById('result_value_desc'); const btnAdd=document.getElementById('add'); const btnSubtract=document.getElementById('sub'); const btnTotal=document.getElementById('total'); const btnPortion=document.getElementById('portion'); const btnSimulate=document.getElementById('simulate'); const cSimulationResult=document.getElementById('c_result_value'); const fSimulationResult=document.getElementById('f_result_value'); const cSimulationQuota=document.getElementById('c_quota_x'); const fSimulationQuota=document.getElementById('f_quota_x'); const cSimulationQuotaValue=document.getElementById('c_quota_value'); const fSimulationQuotaValue=document.getElementById('f_quota_value'); const economyValue=document.getElementById('economy'); let currentCreditIndex=1; let currentType=dataImovel; let currentSimulationType='total';function updateCreditValue(){ const credit=currentType[currentCreditIndex][0]; const quota=currentType[currentCreditIndex][1];valueText.textContent=currentSimulationType==='total'?credit:quota;}function handleAddClick(){if(currentCreditIndex<currentType.length-1){currentCreditIndex++;updateCreditValue();}}function handleSubtractClick(){if(currentCreditIndex>1){currentCreditIndex--;updateCreditValue();}}btnSimulate.addEventListener('click',()=>{simulateLoan(currentType);});function simulateLoan(currentType){document.getElementById('loading').classList.add('loading');document.getElementById('spinner').classList.add('spinner');setTimeout(()=>{ const creditValue=valueText.textContent; const credit=currentType[currentCreditIndex][0]; 
 const quotaValue=currentType[currentCreditIndex][1]; const planValue=currentType[currentCreditIndex][2];valueResult.textContent=creditValue;cSimulationResult.textContent=creditValue;cSimulationQuota.textContent=planValue.toLowerCase()+' de';cSimulationQuotaValue.textContent=quotaValue;fSimulationQuotaValue.textContent=quotaValue;valueResultDesc.textContent='(valor total)';if(planValue.toLowerCase()==='50x'){fSimulationQuota.textContent='100x de';}if(planValue.toLowerCase()==='200x'){fSimulationQuota.textContent='300x de';}function formatCurrency(value){return value.toLocaleString('pt-BR',{style:'currency',currency:'BRL',minimumFractionDigits:2,});} const quotaNum=parseFloat(quotaValue.replace(/[^0-9,.]/g,'').replace(',','.')); const planNum=parseFloat(fSimulationQuota.textContent.replace(/[^0-9,.]/g,'').replace(',','.')); const simulationResultValue=Math.round(planNum*quotaNum*100);fSimulationResult.textContent=formatCurrency(simulationResultValue/100); const creditToNum=parseInt(creditValue.replace(/[^0-9]/g,'').replace(',','.')); const differenceValue=Math.round((simulationResultValue-creditToNum));economyValue.textContent=formatCurrency(differenceValue/100);if(currentSimulationType!=='total'){valueResultDesc.textContent='(valor da parcela)';cSimulationResult.textContent=credit;}document.getElementById('loading').classList.remove('loading');document.getElementById('spinner').classList.remove('spinner');},500);}btnTotal.addEventListener('click',()=>{if(currentSimulationType!=='total'){currentSimulationType='total';btnTotal.classList.add('selected');btnPortion.classList.remove('selected');updateCreditValue();}});btnPortion.addEventListener('click',()=>{if(currentSimulationType!=='portion'){currentSimulationType='portion';btnTotal.classList.remove('selected');btnPortion.classList.add('selected');updateCreditValue();}});btnAdd.addEventListener('click',handleAddClick);btnSubtract.addEventListener('click',handleSubtractClick);updateCreditValue(); const houseBtn=document.getElementById('houseBtn'); const carBtn=document.getElementById('carBtn');function handleTypeClick(event){ const clickedBtn=event.currentTarget;if(clickedBtn.classList.contains('active')){return;}document.querySelector('.type_selector.active').classList.remove('active');clickedBtn.classList.add('active');if(clickedBtn===houseBtn){currentType=dataImovel;}else if(clickedBtn===carBtn){currentType=dataAuto;}currentCreditIndex=1;updateCreditValue();}btnType.forEach(btn=>{btn.addEventListener('click',handleTypeClick);});handleTypeClick({currentTarget:houseBtn});
```

# Licença

Este projeto está licenciado sob os termos da [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Para mais detalhes, consulte o arquivo [LICENSE](/LICENSE).