import pyautogui as pa
import time


roteiro=[
"Aldeão 1: Acha que está aí?",
"Aldeão 2: Tudo bem. Vamos lá!",
"Aldeão 1: Uau. Espera aí. Você sabe o que essa coisa pode fazer com você?",
"Aldeão 3: Sim, ele moerá seus ossos para ganhar o pão.",
"(Shrek ri, revelando-se atrás da multidão)",
"Shrek: Sim, bem, na verdade, seria um gigante.",
"(A multidão grita)",
"Shrek: Agora, ogros... ah, eles são muito piores. Eles vão fazer uma roupa com a sua pele recém-descascada.",
"(Shrek se aproxima lentamente enquanto os moradores recuam com medo)",
"Aldeão: Não!",
"Shrek: Eles vão raspar seu fígado. Espremer a geleia dos seus olhos! Aliás, fica muito bom com torrada.",
"Aldeão 1: Para trás! Para trás, fera! Para trás! Estou avisando!",
"(O aldeão acena com sua tocha na frente do rosto de Shrek. Shrek lambe os dedos casualmente e aperta a chama, apagando a tocha. O aldeão a deixa cair)",
"Aldeão 1: Certo.",
"(Shrek aterroriza a multidão com um rugido assustador, sua saliva apagando todas as tochas restantes. Ele limpa a boca e espera os aldeões pararem de gritar)",
"Shrek: (sussurrando) Essa é a parte em que você foge.",
"Aldeões: (GRITANDO!!!)",
"(Shrek ri enquanto os homens largam suas tochas e forcados e fogem o mais rápido que podem)",
"Shrek: E fique longe!",
"(Ele olha para baixo e pega um cartaz de procurado deixado por um dos moradores. Ele o lê em voz alta)",
"SHREK: \"Procura-se. Criaturas de contos de fadas\".",
"(Ele suspira e vai embora, deixando o cartaz cair no chão)",
"O DIA SEGUINTE - FLORESTA\nCriaturas de contos de fadas são acorrentadas e conduzidas para dentro de carroças pelos Guardas Duloc . O Capitão dos Guardas Duloc senta-se à mesa e paga a uma fila de pessoas suas recompensas por entregarem as criaturas de contos de fadas. Entre os que aguardam na fila estão Peter Pan , que carrega Sininho em uma gaiola, Gepeto , que carrega Pinóquio , e um fazendeiro carregando os Três Porquinhos .",
"Guarda: Tudo bem. Este está cheio. Leve-o embora! Mexa-se. Vamos! Levante-se!",
"O Capitão: Próximo!",
"Guarda: (Pegando a vassoura da bruxa ) Me dá isso! Seus dias de voar acabaram! (quebra a vassoura ao meio)",
"O Capitão: São 20 moedas de prata para a bruxa. Próximo!",
"(O capitão entrega a recompensa ao aldeão que entregou a bruxa. O aldeão murmura para si mesmo)",
"Aldeão: Péssimas 20 peças.",
"Guarda: Levante-se! Vamos!",
"(Esperando na fila está o Burro na coleira e seu dono. Ele olha horrorizado para a bruxa e um grupo de anões sendo colocados em uma carroça)",
"Guarda: Senta aí! Fica quieto!",
"( Mamãe Urso e Papai Urso estão trancados em gaiolas gigantes, com o Ursinho em sua própria gaiola.)",
"Ursinho: (chorando) Esta gaiola é muito pequena.",
"Burro: (Para o dono) Por favor, não me denuncie. Nunca mais serei teimoso. Eu posso mudar. Por favor! Me dê outra chance!",
"Velha: Ah, cala a boca. (dá um tapa no burro)",
"Capitão: Próximo! O que você tem?",
"Gepeto: Este pequeno boneco de madeira.",
"Pinóquio: Eu não sou um fantoche, sou um menino de verdade. (seu nariz cresce)",
"O Capitão: 5 xelins pelo brinquedo possuído. Leve-o embora.",
"Pinóquio: Pai, por favor! Não deixe que eles façam isso! Me ajude!",
"(Geppetto pega o dinheiro e vai embora. A velha se aproxima da mesa)",
"Capitão: Próximo! O que você tem?",
"Velha: Bem, eu tenho um burro falante.",
"Capitão: Certo. Bem, isso vale 10 xelins. Se você puder provar.",
"Velha: Ah, vá em frente, rapazinho. (Burro fica em silêncio)",
"O Capitão: Bem?",
"Velha: Ah, ah, ele só... ele só está um pouco nervoso. Ele é mesmo um tagarela. (Dá outro tapa no Burro) Fala, seu idiota, fala!",
"O Capitão: É isso. Já ouvi o suficiente. Guardas!",
"Velha: Não, não, ele fala! Ele fala mesmo. (Mexendo os lábios do Burro) Eu falo. Eu adoro falar. Sou a coisa mais falante que você já viu.",
"O Capitão: Tire-a da minha vista.",
"Velha: Não, não! Eu juro! Ah! Ele fala!",
"(Os guardas agarram a velha, que luta com eles. Uma de suas pernas voa e chuta Sininho para longe das mãos de Peter Pan, e sua gaiola cai na cabeça do Burro. Ele é salpicado com pó de fada e começa a flutuar para cima)",
"Burro: Ei! Eu consigo voar!",
"Peter Pan: Ele pode voar!",
"Os 3 Porquinhos: Ele sabe voar!",
"O Capitão: Ele consegue falar!?",
"Burro: Ha, ha! É isso mesmo, idiota! Agora sou um burro voador e falante. Você já deve ter visto uma mosca doméstica, talvez até uma supermosca, mas aposto que nunca viu um burro voar. Ha, ha! (O efeito do pó mágico começa a passar.) Uh-oh. (Ele cai do ar e atinge o chão com um baque.)",
"O Capitão: Prendam-no!",
"(O burro desvia dos guardas que tentam agarrá-lo e corre mais para dentro da floresta)",
"Guardas: Atrás dele! Ele está fugindo! Peguem-no! Por aqui! Virem!",
"(O burro escapa para o interior da floresta e bate de cabeça no traseiro de Shrek. Shrek se vira para ver quem esbarrou nele e encara o burro. O burro parece assustado com Shrek por um momento, mas rapidamente se esconde atrás dele depois de ver que os guardas o alcançaram.)",
"O Capitão: Você aí! Ogro!",
"Shrek: Sim?",
"O Capitão: Pela ordem de Lorde Farquaad, estou autorizado a prender vocês dois e... (Shrek se aproxima lentamente do grupo de guardas, os guardas visivelmente assustados por ele) transportá-los para... uma instalação... de reassentamento... designada?",
"Shrek: Sério? Você e qual exército? (sorri)",
"(O Capitão olha para trás e vê que todos os outros guardas o abandonaram. O Capitão abaixa o rabo e sai correndo. Shrek balança a cabeça e começa a caminhar de volta para seu pântano. Burro, impressionado com Shrek, o segue)",
"Burro: Posso te dizer uma coisa? Escuta, você foi realmente incrível aqui atrás. Incrível!",
"Shrek: Você está falando comigo... (ele se vira e o Burro some)? (ele se vira e o Burro está bem na frente dele) Uau!",
"Burro: Sim. Eu estava falando com você. Posso te dizer que você foi ótimo lá atrás? Nossa, esses guardas! Eles achavam que eram tudo isso. Aí você apareceu e bum! Eles estavam tropeçando como bebês na floresta. Isso me fez sentir muito bem.",
"Shrek: (irritado) Ah, isso é ótimo. Sério.",
"Burro: Cara, é bom ser livre.",
"Shrek: Agora, por que você não vai comemorar sua liberdade com seus amigos? Hum?",
"Burro: Mas, uh, eu não tenho amigos. E eu não vou sair por aí sozinho. Ei, espera aí! Tive uma ótima ideia! Vou ficar com você. Você é uma máquina de luta verde e malvada. Juntos, vamos dar um susto em qualquer um que cruzar o nosso caminho.",
"(Shrek se vira e olha para o Burro por um momento antes de rugir alto em seu rosto)",
"Burro: Nossa! Isso foi realmente assustador. Se não se importa que eu diga, se isso não funcionar, seu hálito certamente resolverá o problema, porque você definitivamente precisa de um Tic Tac ou algo assim, porque seu hálito fede!",
"(Shrek vai embora. O burro reaparece à sua frente, pendurado em um tronco caído)",
"Burro: Cara, você quase queimou os pelos do meu nariz, igual daquela vez... (Shrek cobre a boca, mas Burro continua falando. Shrek tira a mão) ...aí eu comi umas frutas podres. Eu estava com gases fortes saindo do meu traseiro naquele dia.",
"Shrek: Por que você está me seguindo?",
"Burro: Vou te dizer o porquê. (cai do tronco. Canta) \"Porque estou sozinho, Não há ninguém aqui ao meu lado, (Shrek geme) Meus problemas acabaram, Não há ninguém para zombar de mim, Mas você tem que ter amigos...\"",
"Shrek: (Gritando) Pare de cantar! (pega o Burro pelas orelhas e pelo rabo) Bem, não é de se espantar que você não tenha amigos! (o larga) Burro: Nossa. Só um amigo de verdade seria tão honesto assim.",
"Shrek: Escuta, burrinho. Olha só para mim. O que eu sou?",
"Burro: (olha para Shrek, abraço amigável?) Uh...muito alto?",
"Shrek: Não! Eu sou um ogro! Sabe, \"Pegue sua tocha e seus forcados!!\". Isso não te incomoda?",
"Burro: (balança a cabeça) Não.",
"Shrek: (surpreso) Sério?",
"Burro: Sério, sério.",
"Shrek: (surpreso) Ah.",
"Burro: Cara, eu gosto de você. Qual é o seu nome?",
"Shrek: Hum, Shrek.",
"Burro: Shrek? Bom, sabe o que eu gosto em você, Shrek? Você tem aquele jeito de \"não me importo com o que ninguém pensa de mim\". Eu gosto disso. Eu respeito isso, Shrek. Você é legal. (Eles vêm de uma colina com vista para o pântano do Shrek) Uau, olha só! Quem ia querer morar num lugar desses?",
"Shrek: (irritado) Essa seria minha casa.",
"Burro: Ah! E é lindo! Simplesmente lindo. Você sabe que é um ótimo decorador. É incrível o que você fez com um orçamento tão modesto. Gostei daquela pedra. Que pedra bonita. (olha para as placas de \"proibido entrar\" do Shrek) Acho que você não recebe muita gente, né?",
"Shrek: Eu gosto da minha privacidade.",
"Burro: Sabe, eu também. Essa é outra coisa que temos em comum. Tipo, eu odeio quando você coloca alguém na sua cara. Você tenta dar uma indireta e a pessoa não vai embora. E fica aquele silêncio constrangedor, sabe? (silêncio constrangedor) Posso ficar com você?",
"Shrek: Uh, o quê?",
"Burro: Posso ficar com você, por favor?",
"Shrek: (sarcasticamente) Claro!",
"Burro: Sério?",
"Shrek: Não.",
"Burro: Por favor! Eu não quero voltar para lá! Você não sabe o que é ser considerado uma aberração. (Burro empurra o Shrek contra a porta) Bem, talvez você saiba. Mas é por isso que temos que ficar juntos. Você tem que me deixar ficar! Por favor! Por favor!",
"Shrek: Certo. Certo! Mas só uma noite.",
"Burro: Ah! Obrigado! (corre para dentro da cabana)",
"Shrek: Ah! O que você... não! (Burro pula em uma cadeira.) Não!",
"Burro: Isso vai ser divertido! Podemos ficar acordados até tarde, trocando histórias masculinas, e de manhã... eu vou fazer waffles.",
"Shrek: (rosna de frustração)",
"Burro: Onde eu durmo?",
"Shrek: (irritado) Lá fora!",
"Burro: Ah, bom, acho que está tudo bem. Quer dizer, eu não te conheço, e você não me conhece, então acho que lá fora é melhor, sabe? Aqui vou eu. Boa noite. (Shrek bate a porta, fechando o Burro do lado de fora) Quer dizer, eu gosto de ar livre. Eu sou um burro. Eu nasci ao ar livre. Vou ficar sentado sozinho lá fora, eu acho, sabe. Sozinho, lá fora. Estou completamente sozinho... não tem ninguém aqui do meu lado...",
"A CASA DE SHREK - NOITE\n(Shrek está se preparando para o jantar. Ele se senta, acende uma vela feita com sua própria cera de ouvido e começa a comer. Burro olha para dentro pela janela e então se deita perto da porta da frente. Shrek está prestes a dar uma mordida quando ouve um rangido. Ele se levanta bufando)",
"Shrek: (para o Burro) Achei que tinha te dito para ficar lá fora!",
"Burro: (da janela) Estou lá fora!",
"(Shrek ouve um barulho vindo de dentro e se vira para encontrar a fonte. Ele vê várias sombras se movendo e olha ao redor. Ele vê os 3 ratos cegos em sua mesa)",
"Rato 1: Bem, senhores, é muito longe da fazenda, mas que escolha temos?",
"Rato 2: Não é o lar, mas vai servir bem.",
"Gorder: (pulando em uma lesma) Que cama linda.",
"Shrek: Peguei você. (agarra Gorder, mas erra quando ele escapa e cai em seu ombro)",
"Gorder: Encontrei um pouco de queijo. (morde a orelha de Shrek)",
"Shrek: Ai! (tenta agarrá-lo)",
"Gorder: Blah! Que coisa horrível. (pula para a mesa)",
"Rato Cego: É você, Gorder?",
"Gorder: Como você sabia?",
"Shrek: Chega! (ele pega os três ratos) O que você está fazendo na minha casa? (Ele é empurrado por trás e deixa os ratos caírem) Ei!",
"(Shrek se vira e vê que os 7 anões colocaram Branca de Neve , dormindo em seu caixão de vidro, sobre a mesa)",
"Shrek: Oh, não, não, não. Morra, fora da mesa! (empurra o caixão para longe)",
"Anão: Onde vamos colocá-la? A cama está ocupada.",
"Shrek: (confuso) Hein?",
"(Shrek caminha até o quarto e abre a cortina. O Lobo Mau está deitado na cama)",
"Lobo: O quê?",
"(Shrek agora segura o Lobo Mau pela gola e o arrasta até a porta da frente)",
"Shrek: Eu moro num pântano. Coloco placas. Sou um ogro assustador! O que eu preciso fazer para ter um pouco de privacidade?!",
"(Ele abre a porta da frente e joga Lobo para fora. Ele vê que uma horda de criaturas de contos de fadas montou acampamento em seu pântano)",
"Shrek: Oh, não. Oh, não. Não! Não! (Ele desvia de um grupo de bruxas voando em vassouras)",
"(Um dos netos da Velha Senhora briga entre si, o Flautista está tocando sua flauta e os ratos estão todos correndo em sua direção, o Ursinho chora enquanto o Papai Urso o confronta na fogueira.)",
"Shrek: O QUE VOCÊ ESTÁ FAZENDO NO MEU PÂNTANO?!?!",
"(A voz de Shrek ecoa por todo o acampamento e todos ficam em silêncio. Suspiros são ouvidos por todos os lados. As 3 Fadas Boas se escondem dentro de uma tenda e os gnomos gritam \"uau\" e se abraçam)",
"Shrek: Certo, saiam daqui. Todos vocês, mexam-se! Vamos! Vamos! Hapaya! Hapaya! Ei!",
"Anões: Depressa. Vamos!",
"(Mais anões correm para dentro da casa e fecham a porta atrás deles)",
"Shrek: Não, não! Não, não. Não aí! Não aí!",
"(Shrek mexe na maçaneta da porta, incapaz de abri-la. Ele lança um olhar irritado para o Burro)",
"Burro: Ei, não olhe para mim. Eu não os convidei.",
"Pinóquio: Nossa, ninguém nos convidou.",
"Shrek: O quê?!",
"Pinóquio: Fomos forçados a vir aqui!",
"Shrek: Por quem?!",
"Porquinho: Lorde Farquaad. Ele bufou, bufou e... assinou um aviso de despejo.",
"Shrek: (suspira) Tudo bem. Quem sabe onde esse... \"Farquaad\" está?",
"(A multidão fica boquiaberta ao ouvir a menção de Lord Farquaad. Ninguém responde)",
"Burro: Ah, eu sei. Eu sei onde ele está!",
"Shrek: Alguém mais sabe onde encontrá-lo?",
"(O Ursinho levanta a mão, mas o Papai Urso rapidamente a abaixa. O Lobo e um mago apontam um para o outro)",
"Shrek: Alguém?",
"Burro: Eu! Eu!",
"Shrek: Alguém?",
"Burro: (pulando para cima e para baixo) Oh! Oh, me pegue! Oh, eu sei! Eu sei! Eu, eu!",
"Shrek: (suspira) Certo, tudo bem. Atenção, pessoal... coisas de contos de fadas. Não fiquem à vontade! Suas boas-vindas estão oficialmente esgotadas! Aliás, vou ver esse Farquaad agora mesmo e tirar vocês da minha terra e levá-los de volta para onde vieram!",
"(Após um breve silêncio, a multidão irrompe em gritos e aplausos. Essa não era a intenção de Shrek. Um grupo de pássaros coloca uma capa feita de flores em volta dos ombros de Shrek, para seu aborrecimento)",
"Shrek: Oh! (para o Burro) Você! Você vem comigo.",
"(Shrek joga a capa no chão, enquanto os pássaros retornam para colocar uma coroa de flores na cabeça do Burro. Eles passam pela multidão)",
"Burro: Tudo bem, é isso que eu gosto de ouvir, cara. Shrek e Burro, dois amigos leais, embarcam em uma aventura alucinante pela cidade grande. Adorei!",
"Burro: (cantando) \"Na estrada outra vez...\", cante comigo, Shrek!",
"(enquanto eles se afastam da multidão, Shrek pega a tocha de um anão que os aplaude, mas ele se recusa a soltá-la. Shrek sacode a tocha até que o anão caia em um lago)",
"Burro: \" Mal posso esperar para pegar a estrada novamente. \"",
"Shrek: O que eu disse sobre cantar? (tira a guirlanda da cabeça do Burro)",
"Burro: Posso assobiar?",
"Shrek: Não.",
"Burro: Bem, posso cantarolar?",
"Shrek: (irritado) Tudo bem, cantarole.",
"(Burro começa a cantarolar 'On the Road Again'. A dupla caminha noite adentro com a tocha de Shrek iluminando o caminho)"
]

# DULOC - MASMORRA
# (Um homem mascarado está servindo um copo de leite. Outro homem é mostrado caminhando pelo corredor em direção a um conjunto de portas. Quando ele é deixado entrar na sala por dois guardas, podemos ver que o homem é anormalmente baixo. O homem mascarado está mergulhando o que parece ser uma pessoa pequena no copo de leite)

# Lorde Farquaad: (dando um passo à frente) Chega. Ele está pronto para falar.

# Gingy é puxado para fora do leite por Thelonious e jogado em uma assadeira. Lorde Farquaad ri maldosamente enquanto caminha até a mesa. Quando ele chega à mesa, vemos que ele é baixo demais para enxergar por cima dela. Ele pigarreia e a mesa é abaixada.

# Lorde Farquaad: (Ele pega as pernas decepadas do Gingy e brinca com elas) Corra, corra, corra, o mais rápido que puder. Você não pode me pegar. Eu sou o homem-biscoito de gengibre!

# Gingy: Você é um monstro!

# Lorde Farquaad: Eu não sou o monstro aqui, você é. (joga uma perna em Gingy) Você e o resto desse lixo de conto de fadas, envenenando meu mundo perfeito. (esfarela a outra perna até virar pó) Agora, me diga! Onde estão os outros?!

# Gingy: Coma-me! (cospe no olho esquerdo de Lord Farquaad)


# Lorde Farquaad: Argh! Eu tentei ser justo com vocês, criaturas. Agora minha paciência chegou ao fim! Digam-me ou eu...! (Ele pega um dos botões de bala de goma do Gingy)

# Gingy: (Triste) Não, não, os botões não. Não os meus botões de bala de goma!

# Lorde Farquaad: Tudo bem então. Quem os está escondendo?

# Gingy: Certo, vou te contar. Você conhece o homem dos muffins?

# Lord Farquaad: O homem dos muffins?

# Gingy: O homem dos muffins.

# Lorde Farquaad: Sim, eu conheço o vendedor de muffins. Quem mora na Drury Lane ?

# Gingy: Bem, ela é casada com o homem dos muffins.

# Lord Farquaad: (Chocado) O homem dos muffins?

# Gingy: O homem dos muffins!

# Lord Farquaad: Ela é casada com o homem dos muffins.

# (Uma porta se abre e o Capitão dos Guardas Duloc entra)

# O Capitão: Meu senhor! Nós o encontramos.

# Lorde Farquaad: Então o que está esperando? Traga-o!

# (Mais guardas entram carregando um objeto coberto por um lençol. Eles o penduram na parede e o Capitão remove o lençol. É o Espelho Mágico . Todos ficam boquiabertos)

# Gingy: (Olhos arregalados) Ohhhh...

# Lorde Farquaad: Espelho mágico...

# Gingy: Não conte nada a ele! (Lorde Farquaad o joga da mesa em uma lata de lixo para silenciá-lo) Não!

# Lorde Farquaad: Boa noite. Espelho, espelho meu, este não é o reino mais perfeito de todos?

# Espelho Mágico: Bem, tecnicamente você não é um rei.

# Lorde Farquaad: Uh, Thelonious? (Thelonious levanta um espelho de mão e o quebra com o punho como uma ameaça ao Espelho Mágico) O que você estava dizendo?

# Espelho Mágico: O que quero dizer é que você ainda não é rei . (risos) Mas você pode se tornar um. Tudo o que você precisa fazer é se casar com uma princesa.

# Lorde Farquaad: Continue.

# Espelho Mágico: (rindo nervosamente) Então, sente-se e relaxe, meu senhor, porque chegou a hora de conhecer as solteiras cobiçadas de hoje. E... aqui estão elas!

# (Uma animada música de game show começa a tocar. Usando a si mesmo como uma tela, o Espelho Mágico revela três retratos sombrios de princesas. Lorde Farquaad parece confuso, mas observa em silêncio)

# Espelho Mágico: A solteira número 1 é uma reclusa que sofre abuso mental e vem de um reino muito, muito distante. Ela gosta de sushi e banheiras de hidromassagem a qualquer hora! Seus hobbies incluem cozinhar e limpar para suas duas irmãs malvadas. Por favor, dê as boas-vindas... à Cinderela !

# (Uma imagem de Cinderela fazendo tarefas domésticas muda para um retrato de Cinderela em seu vestido de baile colocando o sapatinho de cristal. Lorde Farquaad olha para ela com aprovação e o Capitão bate palmas)

# Espelho Mágico: A solteira número 2 é uma garota de capa vinda da terra da fantasia. Embora viva com outros 7 homens, ela não é fácil.

# (Uma imagem dos 7 Anões aparece na tela. Os guardas riem da piada do Espelho)

# Espelho Mágico: Basta beijar seus lábios mortos e congelados e descobrir a tensão que ela tem. Vamos lá, aplaudam a Branca de Neve!

# (O espelho mostra um retrato de Branca de Neve dormindo. Lorde Farquaad parece ainda mais satisfeito, e todos os outros aplaudem desta vez)

# Espelho Mágico: E por último, mas certamente não por último, a solteira número 3 é uma ruiva fogosa de um castelo guardado por dragões, cercado por lava fervente!

# (O espelho mostra a imagem de um dragão gigante, cruel e selvagem, ao lado de uma torre e, em seguida, de um castelo gigante cercado por lava. Um fogo brilhante brilha na tela e Lorde Farquaad cobre os olhos. Isso não parece deter seu interesse)

# Espelho Mágico: Mas não deixe que isso te acalme. Ela é uma pistola carregada que gosta de piña coladas e de ser pega na chuva. Sua por me salvar, Princesa Fiona !

# (O espelho mostra um retrato da Princesa Fiona encostada na janela de sua torre. Mais uma vez todos os outros aplaudem)

# Espelho Mágico: Então, será: solteira número 1, solteira número 2 ou solteira número 3?

# (Os espelhos passam pelo retrato de cada princesa. Os guardas gritam números diferentes enquanto Lorde Farquaad tenta freneticamente decidir)

# Guardas: 2! 2! 3! 3! 2! 2! 3!

# Lord Farquaad: (para si mesmo) 2? 3? 1? (choraminga) 3?

# Thelonius: 3! (levanta 2 dedos em vez de 3) Escolha o número 3, meu senhor!

# Lorde Farquaad: Certo, certo! Hum... número 3!

# Espelho Mágico: Lorde Farquaad, você escolheu a Princesa Fiona.

# (Aplausos calorosos irrompem dos guardas. Lorde Farquaad fica cativado pelo retrato de Fiona)

# Lorde Farquaad: Princesa... Fiona... ela é perfeita. Tudo o que preciso fazer é encontrar alguém que possa ir...

# Espelho Mágico: Mas eu provavelmente deveria mencionar a coisinha que acontece à noite.

# (Lord Farquaad não escuta o espelho, muito ocupado formulando um plano)

# Lorde Farquaad: Eu farei isso.

# Espelho Mágico: Sim, mas depois do pôr do sol...

# Lorde Farquaad: Silêncio! Farei desta Princesa Fiona minha rainha, e Duloc finalmente terá o rei perfeito! Capitão, reúna seus melhores homens. Vamos ter um torneio! (sorriso maligno)

# REINO DULOC - EXTERIOR
# (Shrek e Burro saem do campo do lado de fora do estacionamento Duloc)

# Burro: Mas é isso. É isso aí. É o Duloc. Eu disse que ia encontrar.

# (Os dois olham para o Castelo Duloc , um edifício que se eleva sobre o resto do reino)

# Shrek: Então, esse deve ser o castelo do Lorde Farquaad.

# Burro: É, é esse o lugar.

# Shrek: Você acha que talvez ele esteja compensando alguma coisa?

# (Shrek ri, mas depois geme porque Burro não entende a piada. Ele continua andando pelo estacionamento)

# Burro: Ei, espera aí. Espera aí, Shrek.

# Homem: Depressa, querida. Estamos atrasados. Depressa!

# (Um homem e uma mulher correm pela entrada do castelo. Em frente ao portão há uma série de cordas penduradas em um labirinto para controlar a multidão. Um mascote usando uma cabeça gigante parecida com Lord Farquaad está no final da fila. Shrek e Burro trocam olhares)

# Shrek: Ei, você!

# (O mascote grita ao ver Shrek e começa a correr pelo caminho de corda para chegar ao portão da frente)

# Shrek: Espera aí. Olha, eu não vou te comer. Eu só... eu só...

# (Shrek suspira frustrado e então começa a abrir caminho através das cordas. O mascote bate em uma parede e desmaia. Shrek empurra a catraca da entrada, mas Burro fica preso nela e cai no chão com um baque. Burro sorri timidamente e Shrek suspira irritado)

# DULOC - INTERIOR
# (Shrek e Burro olham ao redor da praça, que está deserta. As árvores e a grama estão bem aparadas e as fileiras de casas parecem todas exatamente iguais. Uma música alegre toca baixinho em um conjunto de alto-falantes)

# Shrek: Está quieto. Quieto demais. Cadê todo mundo?

# Burro: Ei, olha isso!

# (O burro corre e puxa uma alavanca que está presa a uma caixa marcada como "Informações". A música toca e então as portas da caixa se abrem. Há pequenas pessoas de madeira lá dentro enquanto elas começam a cantar)

# Pessoas de Madeira: (CANTANDO) Bem-vindos a Duloc, uma cidade tão perfeita / Aqui temos algumas regras, vamos estabelecê-las / Não faça barulho, fique na linha e nos daremos bem / Duloc é o lugar perfeito / Por favor, fique longe da grama / Engraxe seus sapatos, limpe seu... rosto / Duloc é, Duloc é / Duloc é um lugar perfeito.

# (De repente, uma câmera tira uma foto de Shrek e Burro, ambos ficam estupefatos)

# Burro: Uau! Vamos fazer isso de novo!

# (Burro se prepara para correr e puxar a alavanca novamente, mas Shrek rapidamente o agarra pelo rabo)

# Shrek: Não! Não! Não, não, não! (sussurra) Não.

# (Eles ouvem uma fanfarra de trombeta ao longe e vão investigar. Uma voz soa à distância)

# Lorde Farquaad: Bravos cavaleiros! Vocês são os melhores e mais brilhantes de toda a terra, e hoje um de vocês se mostrará melhor, mais brilhante e mais brutal do que todos os outros.

# (Enquanto Shrek e Burro caminham pelo túnel para entrar na arena, Burro cantarola a música tema de Duloc)

# Shrek: Tudo bem, você está indo no caminho certo para um traseiro amassado.

# Burro: Desculpe por isso.

# ARENA
# (No centro de uma arena semelhante a um estádio, os Cavaleiros Duloc estão reunidos enquanto uma grande multidão de cidadãos assiste das arquibancadas. Cavalos, barris de cerveja, alvos de flechas e outros equipamentos estão espalhados. Farquaad está no topo de uma sacada alta, ladeado por dois guardas, se dirigindo à multidão. Shrek e Burro saem para a arena, mas não parecem ser notados)

# Lorde Farquaad: Esse campeão terá a honra — não, não — o privilégio de ir em frente e resgatar a adorável Princesa Fiona da fortaleza flamejante do dragão. Se, por qualquer motivo, o vencedor não for bem-sucedido, o segundo colocado tomará seu lugar. E assim por diante. Alguns de vocês podem morrer, mas é um sacrifício que estou disposto a fazer.

# (A multidão grita e aplaude. Shrek olha ao redor, notando um homem segurando um cartão com a inscrição "APLAUSOS" para a multidão.)

# Lorde Farquaad: Que o torneio comece!

# (Shrek marcha através dos Cavaleiros Duloc, que recuam enojados ao notá-lo)

# Lorde Farquaad: Oh! O que é isso? É horrível!

# (A multidão fica boquiaberta e em silêncio)

# Shrek: Ah, isso não é muito legal (olha para o Burro e depois para Lorde Farquaad) É só um burro.

# (O burro parece confuso, a piada mais uma vez não foi compreendida)

# Lorde Farquaad: De fato. Cavaleiros, novo plano! Aquele que matar o ogro será nomeado campeão! Ataquem-no!

# (Lord Farquaad aponta para Shrek. Os Cavaleiros Duloc sacam suas armas e se aproximam lentamente de Shrek enquanto ele recua, enquanto a multidão os aplaude)

# Multidão: Peguem ele!

# Shrek: Ah, ei! Vamos lá! Espere aí. (Ele esbarra em uma mesa e nota canecas de cerveja.)

# Multidão: Vá em frente! Peguem ele!

# Shrek: (levanta uma caneca de cerveja) Não podemos resolver isso tomando uma cerveja?

# Multidão: Matem a fera!

# Shrek: Não? Tudo bem então. (bebe a cerveja de um só gole) Vamos!

# (Shrek pega a caneca e quebra a torneira do grande barril de cerveja atrás dele. A cerveja sai correndo, derrubando os cavaleiros e molhando o chão com lama. Shrek desliza pelos cavaleiros e usa uma lança como um taco de hóquei para derrubar um deles. O tema Freaks and Geeks toca enquanto o Burro pula em um dos maiores barris de cerveja. Ele se solta das cordas e começa a rolar. O Burro consegue esmagar 2 cavaleiros na lama e rola sobre outro grupo de cavaleiros correndo atrás de Shrek. Shrek pula sobre um conjunto de cordas que parece formar um ringue de luta livre. Shrek usa as cordas para se lançar em 2 cavaleiros, derrubando-os com os braços. A multidão vaia. Shrek dá um chute em um cavaleiro e depois dá um golpe no corpo de outro. Um cavaleiro vem de trás de Shrek com sua lança pronto para atacar. A multidão fica boquiaberta, mas antes que ele possa fazer um movimento, Shrek o coloca em um retenção completa de Nelson)

# Burro: Ei, Shrek, me pega! Me pega!

# (Shrek leva o cavaleiro até o Burro, que se apoia nas cordas e dá uma cabeçada no cavaleiro. Shrek sobe nas cordas e interage com a multidão, que agora começa a torcer por Shrek e Burro. Shrek fica em cima das cordas e acena para os aplausos da multidão)

# Shrek: Sim!

# (Um cavaleiro tenta se esgueirar por trás de Shrek, mas não consegue pegá-lo, pois se vira a tempo de vê-lo e pula sobre ele)

# Mulher: A cadeira! Dê a cadeira a ele!

# (Shrek usa uma cadeira dobrável para bater no cavaleiro caído no chão. Shrek derrota mais alguns cavaleiros com facilidade. Shrek pega o último cavaleiro, girando-o sobre sua cabeça e então o joga contra o poste do ringue de luta livre. Burro chuta seu capacete, e o ding soa o fim da luta. Finalmente todos os cavaleiros estão caídos. A plateia vai à loucura. Shrek ri)

# Shrek: Ah, sim! (rosna de alegria, e depois de novo) Obrigada! Muito obrigada! Estou aqui até quinta. Experimente a vitela! Ha, ha! (risos)

# (Lorde Farquaad faz um gesto para os guardas, que apontam suas bestas para Shrek e Burro. A multidão fica boquiaberta e em silêncio. Shrek para de rir)

# Guarda: Devo dar a ordem, senhor?

# Lorde Farquaad: Não, tenho uma ideia melhor. Povo de Duloc! Apresento-lhes o nosso campeão!

# (A multidão aplaude e uma fanfarra toca)

# Shrek: O quê?

# Lorde Farquaad: Parabéns, ogro. Você ganhou a honra de embarcar em uma grande e nobre jornada.

# Shrek: Missão? Já estou em uma missão. Uma missão para recuperar meu pântano.

# Lord Farquaad: Seu pântano?

# Shrek: É, meu pântano! Onde você jogou aquelas criaturas de contos de fadas!

# Lorde Farquaad: De fato. Tudo bem, ogro. Farei um acordo com você. Participe desta missão por mim e eu lhe devolverei o seu pântano.

# Shrek: Exatamente como era?

# Lorde Farquaad: Até o último cogumelo coberto de lodo.

# Shrek: E os invasores?

# Lorde Farquaad: Praticamente desaparecido.

# (Shrek olha para os soldados que ainda apontam suas bestas e então se vira para Lorde Farquaad)

# Shrek: Que tipo de missão?

# CAMPO VEGETAL
# (Shrek e Burro agora estão caminhando pelos campos, afastando-se de Duloc. Shrek está mastigando uma cebola enquanto faz bagunça nos campos)

# Burro: Certo, então deixa eu ver se entendi. Você vai lutar contra um dragão e resgatar uma princesa só para que o Farquaad te devolva um pântano que você só não tem porque ele o encheu de aberrações. É isso mesmo?

# Shrek: Sabe, talvez haja uma boa razão para os burros não falarem.

# Burro: Não entendi. Por que você não usa aquela coisa de ogro nele? Estrangula ele, sitia a fortaleza dele, tritura os ossos dele para ganhar o seu pão, essa coisa toda de ogro.

# Shrek: Ah, já sei. Talvez eu pudesse ter decapitado uma vila inteira e espetado suas cabeças em uma lança, pegado uma faca, aberto seus baços e bebido seus fluidos. Isso parece bom para você?

# Burro: Não, não mesmo, não.

# Shrek: Para sua informação, os ogros são muito mais do que as pessoas pensam.

# Burro: Exemplo?

# Shrek: Exemplo? Certo, hum, ogros são como cebolas. (Ele estende a cebola)

# Burro: (cheira a cebola) Elas fedem?

# Shrek: Sim - - Não!

# Burro: Eles fazem você chorar?

# Shrek: Não!

# Burro: Ah, se você deixá-los no sol, eles ficam todos marrons e começam a brotar pelinhos brancos.

# Shrek: Não! Camadas! Cebolas têm camadas. Ogros têm camadas! Cebolas têm camadas. Entendeu? Nós dois temos camadas. (Ele joga a cebola fora e vai embora)

# Burro: (seguindo o Shrek) Ah, vocês dois têm camadas. Ah. {funga} Sabe, nem todo mundo gosta de cebola. Bolo! Todo mundo adora bolo! Bolos têm camadas.

# Shrek: Não me importa... o que cada um gosta. Ogros não são como bolos. (passa pelo Burro)

# Burro: Sabe o que mais todo mundo gosta? Parfaits. Você já conheceu alguém que, quando você diz: "Vamos comer um parfait", responde: "De jeito nenhum, eu não gosto de parfaits"? Parfaits são deliciosos.

# Shrek: (Gritando) NÃO! Seu burro, irritante e minúsculo animal de carga! Ogros são como cebolas! Fim da história. Tchau. (sussurra) Até mais.

# Burro: Parfaits podem ser a coisa mais deliciosa do planeta inteiro.

# Shrek: Sabe, acho que eu preferia seu cantarolar.

# Burro: Você tem um lenço de papel ou algo assim? Estou fazendo uma bagunça. Só de ouvir a palavra "parfait" já começo a babar.

# (Eles partem. Há uma montagem de sua jornada. Caminhando por um campo ao pôr do sol. Dormindo sob uma lua brilhante. Shrek queima o pé tentando apagar a fogueira, então Burro urina no fogo para apagá-lo. Eles chegam aos arredores de um vulcão gigante e começam a subir)

# Burro: (funga) Ufa! Shrek! Você fez isso? Tem que avisar alguém antes de começar a falar. Fiquei de boca aberta e tudo.

# Shrek: Acredite, Burro, se fosse eu, você estaria morto. (funga) É enxofre. Devemos estar chegando perto.

# Burro: É, enxofre. Não fale nisso, é enxofre. Eu sei o que estou sentindo. Não era enxofre. Também não saiu pedra nenhuma.

# (Eles chegam ao topo da subida e se içam para cima e sobre o cume)

# FORTALEZA DO DRAGÃO - EXTERIOR
# (Shrek e Burro olham para a cratera. A Fortaleza do Dragão se erguia diante deles, um castelo dilapidado, queimado e enegrecido. Empoleirado em um pináculo rochoso, era cercado por um lago aterrorizante de lava derretida. Uma única luz brilha na janela da torre mais alta. Nuvens escuras bloqueiam o céu azul acima deles. Trovões caem e corvos circulando o castelo podem ser ouvidos. É tudo muito sinistro)

# Shrek: Claro, é grande o suficiente, mas olhe a localização. (risos)

# (Shrek pula e se aproxima da ponte, com Burro se juntando a ele atrás)

# Burro: (rindo nervosamente) Ei, Shrek? Ei, lembra quando você disse que ogros têm camadas?

# Shrek: Ah, sim.

# Burro: Bom, tenho uma confissão a fazer (suspira ao ver o esqueleto de um cavalo). Burros não têm camadas de roupa. Nós exibimos o nosso medo bem ali na manga.

# Shrek: Espera aí. Burros não têm mangas.

# Burro: Você sabe o que quero dizer.

# Shrek: Ah, você não pode me dizer que tem medo de altura.

# Burro: Não, só estou um pouco desconfortável por estar em uma ponte frágil sobre um lago de lava fervente!

# Shrek: Vamos, Burro. Estou aqui do seu lado, ok? Para apoio emocional. Vamos encarar isso juntos, um passo de cada vez.

# Burro: Sério?

# Shrek: Sério, sério.

# Burro: Certo, isso me faz sentir muito melhor.

# Shrek: Continue andando. E não olhe para baixo.

# Burro: (nervoso para si mesmo) Certo, não olhe para baixo. Não olhe para baixo. Não olhe para baixo. Continue andando. Não olhe para baixo.

# (O burro acidentalmente pisa em uma tábua podre, que cai na lava ardente abaixo)

# Burro: Shrek! Estou olhando para baixo! (grita) Oh, Deus, eu não consigo fazer isso! Só me solta, por favor!

# Shrek: Mas você já está na metade do caminho.

# Burro: Mas eu sei que metade está segura!

# Shrek: Certo, tudo bem. Não tenho tempo para isso. Volte você.

# (Shrek tenta continuar enquanto Burro tenta voltar para debaixo de Shrek)

# Burro: Shrek, não! Espera!

# Shrek: Só, Burro - - Vamos dançar então, certo? (salta e balança a ponte)

# Burro: Não faça isso!

# Shrek: Ah, me desculpe. Fazer o quê? Ah, isso? (pula a ponte de novo)

# Burro: Sim, isso!

# Shrek: Sim? Sim, faça isso. Certo. (continua pulando e balançando enquanto empurra o Burro pela ponte)

# Burro: Não, Shrek! Não! Pare com isso!

# Shrek: Você disse para fazer! Eu vou fazer.

# Burro: Eu vou morrer. Eu vou morrer. Shrek, eu vou morrer. (pisa em chão firme) Oh!

# Shrek: Está bom, Burro. Está bom. (Caminha em direção ao castelo)

# Burro: Legal. Então, onde está essa dor de cabeça cuspidora de fogo?

# Shrek: Lá dentro, esperando que a resgatemos. (risos)

# Burro: Eu estava falando sobre o dragão, Shrek.

# GUARDA DO DRAGÃO - INTERIOR
# (A dupla começa a caminhar pelos corredores da fortaleza escura e assustadora do dragão. Shrek está cauteloso, enquanto Burro está completamente apavorado. Apenas uma tocha ocasional ilumina o caminho. As passagens estão cheias de ossos, armaduras e armas, provavelmente pertencentes aos muitos cavaleiros malsucedidos que tentaram resgatar a princesa)

# Burro: (sussurra nervosamente) Você está com medo?

# Shrek: Não. Mas... (faz Burro ficar quieto com medo de acordar o dragão)

# Burro: (suspira) Ah, ótimo. Eu também não. (se assusta e suspira) Porque não há nada de errado em ter medo. O medo é uma resposta sensata a uma situação desconhecida. Uma situação perigosa e desconhecida, devo acrescentar. Com um dragão que cospe fogo, devora cavaleiros e cospe fogo. Com certeza não significa que você seja covarde se estiver um pouco assustado. Eu com certeza não sou covarde. Eu sei disso.

# (O burro bate em uma pilha de restos mortais de cavaleiros , derrubando um esqueleto cujo capacete cai na cabeça do burro. A cabeça do esqueleto cai e o burro fica sem fôlego)

# Shrek: Burro, duas coisas, ok? Cala. A boca. Agora vai lá e vê se encontra alguma escada. (Pega o capacete e o coloca)

# Burro: Escadas? Pensei que estávamos procurando a princesa.

# Shrek: (pegando pedaços da armadura) A princesa estará lá em cima, na sala mais alta da torre mais alta.

# Burro: O que faz você pensar que ela estará lá?

# Shrek: Eu li isso em um livro uma vez. (sai andando)

# Burro: Legal. Você cuida do dragão. Eu cuido das escadas. Eu encontro essas escadas. Vou dar uma surra neles também. Essas escadas não vão saber para onde estão indo.

# (Shrek, agora disfarçado como um cavaleiro de armadura brilhante, caminha para dentro do castelo. Burro vagueia na direção oposta, ainda falando sozinho, e abre caminho através de um conjunto gigante de portas)

# Burro: Vou tomar medidas drásticas. Chutar para o meio-fio. Não mexa comigo. Eu sou o mestre das escadas. Eu domino as escadas. Quem me dera ter um degrau aqui. Eu pisaria nele todo.

# (Atrás de uma parede quebrada, um olho gigante se abre para ver um Burro desavisado. Em outro lugar, Shrek vê uma luz na janela de uma torre)

# Shrek: Bem, pelo menos sabemos onde a princesa está. Mas onde está...

# Burro: DRAGÃO!!!!!!

# (O burro grita e sai correndo, desviando por pouco do sopro de fogo do dragão. O dragão persegue o burro, pisoteando a pilha de restos mortais do cavaleiro em seu caminho. Shrek se vira e vê o burro correndo em sua direção com o dragão logo atrás dele)

# Shrek: Burro, cuidado!

# (Shrek consegue agarrar o Burro para tirá-lo do caminho, no momento em que o dragão cospe outra bola de fogo. O Burro cai no chão para evitar outra bola de fogo, que consegue queimar o tufo de sua cauda. O dragão está prestes a comer o Burro quando Shrek agarra sua cauda)

# Shrek: Peguei você!

# (O dragão começa a balançar sua cauda para frente e para trás com Shrek ainda segurando, então o lança no ar. Shrek atravessa o telhado da torre mais alta e entra no quarto de Fiona. Fiona acorda e olha para ele deitado no chão inconsciente. O dragão agora concentra sua atenção em Burro, cuspindo fogo nele e forçando-o a subir em uma ponte de pedra. O dragão derruba partes da ponte até que Burro fique em um pilar solitário)

# Burro: Não. Oh, não, não! (o dragão rosna) Oh, que dentes grandes você tem! (o dragão ruge) Quero dizer, dentes brancos e brilhantes!

# (O dragão faz uma pausa, olha para ele com curiosidade e então sorri. O burro pode estar apenas bajulando e evitando virar comida de dragão)

# Burro: Eu sei que você provavelmente ouve isso o tempo todo da sua comida, mas você deve usar alvejante, porque esse é um sorriso deslumbrante. Percebo um toque de frescor mentolado?

# (O dragão parece ficar lisonjeado com os elogios do Burro)

# Burro: E sabe de mais uma coisa? Sabe de mais uma coisa? Você... Você...

# (O dragão se inclina para frente e olha para o Burro, revelando seus longos cílios e boca pintada de batom. De repente, tudo ficou claro para o Burro)

# Burro: --uma dragãozinha! Ah, claro! Quer dizer, é claro que você é uma dragãozinha. Você exala beleza feminina.

# (O dragão pisca os olhos para ele)

# Burro: O que houve? Tem alguma coisa no seu olho?

# (Dragão sopra um anel de fumaça em forma de coração em direção ao Burro)

# Burro: Ohh. Oh. Oh. Cara, eu adoraria ficar, mas sabe, eu sou, uh... (tosse) Eu sou asmático, e não sei se daria certo se você soprasse anéis de fumaça e coisas assim. Shrek!

# (Dragão o pega pelo rabo com a boca e o carrega alegremente)

# Burro: Não! Shrek! Shrek! Shrek!

# TORRE DE FIONA - INTERIOR
# (Shrek geme ao recuperar a consciência. Ele está de costas para a Princesa Fiona, deitada ereta na cama perto da janela. Embora um pouco assustada, ela fica em êxtase ao ver seu cavaleiro de armadura brilhante. Ela ajeita o vestido, deita-se novamente e rapidamente pega um buquê de flores na mesa lateral. Ela se deita novamente e finge estar dormindo, segurando o buquê contra o peito. Shrek se vira, percebe a princesa e atravessa o quarto até ela. Ele se inclina sobre Fiona e ela franze os lábios. Shrek a segura pelos ombros e a sacode com força)

# Fiona: O qu...O qu...

# Shrek: Acorde!

# Fiona: O quê?!

# Shrek: Você é a Princesa Fiona?

# Fiona: Eu estou... (sorrindo) esperando um cavaleiro tão ousado a ponto de me resgatar.

# Shrek: Ah, que legal. Agora vamos!

# (Shrek se vira para sair e Fiona rapidamente se senta ereta)

# Fiona: Mas espere, Senhor Cavaleiro! Este é o nosso primeiro encontro. Não deveria ser um momento maravilhoso e romântico?

# (ela joga o buquê e se deita novamente, desmaiando)

# Shrek: É, desculpa, moça. Não temos tempo.

# (Shrek volta, puxa o braço de Fiona e a puxa para fora da cama em direção à porta)

# Fiona: Ei, espera aí. O que você está fazendo? Sabe, você devia me levar para fora daquela janela e me jogar por uma corda no seu valente corcel.

# (Shrek puxa a maçaneta da porta apenas para ela quebrar)

# Shrek: Você teve muito tempo para planejar isso, não é?

# Fiona: Hum-hum.

# (Fiona grita quando Shrek de repente quebra a porta com o ombro, ainda segurando o braço dela. Ele desce correndo as escadas da torre com Fiona a tiracolo e pega uma tocha)

# Fiona: Mas temos que saborear este momento! Você poderia recitar um poema épico para mim.

# GUARDA DO DRAGÃO - INTERIOR
# (Shrek e Fiona atravessam a ponte que conecta a torre mais alta ao resto do castelo)

# Fiona: Uma balada? Um soneto! Uma limerique? Ou algo assim!

# (Fiona puxa o braço do aperto de Shrek. Eles param por um momento enquanto Shrek descobre em que direção ir)

# Shrek: Acho que não.

# Fiona: Bem, posso pelo menos saber o nome do meu campeão?

# Shrek: Hum, Shrek.

# Fiona: Senhor Shrek.

# (ela sorri, limpa a garganta e estende um lenço )

# Fiona: Peço que você aceite esse favor como um símbolo da minha gratidão.

# Shrek: Obrigado!

# (Shrek olha o lenço com curiosidade e limpa o rosto sujo de fuligem com ele, deixando-o preto. Ele o devolve para uma Fiona horrorizada, mas antes que ela possa reagir, eles se assustam com o rugido do dragão quando ela o deixa cair no chão)

# Fiona: Você não matou o dragão?!

# Shrek: Está na minha lista de tarefas, agora vamos!

# (Shrek agarra Fiona mais uma vez e sai correndo na direção do rugido do dragão)

# Fiona: Mas isso não está certo! Você deveria atacar, espada em punho, estandarte esvoaçando. Foi o que todos os outros cavaleiros fizeram!

# Shrek: Sim, logo antes de explodirem em chamas!

# (Ele gesticula para o esqueleto de um cavaleiro encostado na parede, com o contorno carbonizado de um homem gravado na pedra atrás dele)

# Fiona: Não é isso que importa! Argh!

# (Fiona solta o braço de Shrek e para de correr. Shrek para para olhar ao redor e se dirige a um conjunto de portas de madeira)

# Fiona: Espera, aonde você vai? A saída é ali!

# (ela aponta o braço para a esquerda e Shrek se vira)

# Shrek: Bem, eu tenho que salvar minha pele.

# Fiona: Que tipo de cavaleiro você é?

# Shrek: Único.

# SALA DO TRONO
# (Shrek abre as portas silenciosamente, saindo para uma sacada de uma sala grande e espaçosa. No centro da sala, Dragon tem Donkey enrolado em sua cauda. Dragon está sentado no chão coberto com uma horda de moedas de ouro e joias)

# Burro: Calma. Calma, querida, por favor. Olha, eu acho que é saudável conhecer alguém por um longo período de tempo. Só, só me chame de antiquado. Eu não quero me precipitar em um... um relacionamento físico. Eu não... não estou emocionalmente pronto para um compromisso, uh, dessa, uh... "magnitude" é realmente a palavra que estou procurando. Magnitude.

# (Dragão acaricia gentilmente Burro com uma única garra)

# Burro: Ei, isso é contato físico indesejado. Ei, o que você está fazendo?

# (Dragon olha para o lustre pendurado acima deles e acende suavemente suas velas com seu sopro de fogo)

# Burro: Tá bom, tá bom. Vamos recuar um pouco e dar um passo de cada vez. Quer dizer, a gente devia mesmo se conhecer primeiro, sabe, como amigos ou até mesmo como correspondentes. Sabe, porque eu viajo bastante, mas adoro receber cartões para ler...

# (Shrek pula da sacada, agarrando uma corrente conectada ao lustre. A corrente não está baixa o suficiente para que ele consiga agarrar o Burro e o manda balançando sobre o Dragão. A corrente balança para trás e acaba balançando-o acima dela)

# Burro: Ah, você sabe, eu adoraria ficar, mas... (O dragão puxa o rabo do Burro com a boca)

# Burro: Ei. Ei, não faça isso! Esse rabo é meu! Esse rabo é meu. Você vai arrancá-lo. Eu não dou permissão para... Ei! O que você vai fazer com isso?

# (Dragão franze os lábios e se prepara para beijar Burro. Shrek olha para cima e percebe que a corrente está presa acima dele. Ele começa a sacudi-la para tentar soltá-la da polia. De repente, a polia se solta e Shrek começa a cair)

# Burro: Ei, agora. De jeito nenhum. Não! Não! Não, não! Não. Não, não, não. Não! Oh!

# (Shrek pousa em Burro e o joga para longe do alcance de Dragão quando ela está prestes a beijá-lo, e agora beija a bunda de Shrek. Ela abre os olhos e ruge. Shrek solta a corrente e o lustre cai sobre sua cabeça, que funciona como uma coleira em volta do pescoço. Ela ruge novamente e Shrek e Burro saem correndo. Eles desviam de uma rajada de fogo de Dragão. Shrek agarra Burro com um braço e então agarra a Princesa Fiona, que entrou na sala, com o outro braço enquanto passa correndo por ela)

# Burro: Olá, princesa!

# Fiona: Ele fala!

# Shrek: Sim, o truque é fazê-lo calar a boca.

# (Todos eles ofegam quando Shrek para de repente, tendo chegado ao fim da sacada, Shrek avista uma coluna caída que formou uma espécie de escorregador. Ele pula nela no momento em que Dragon tenta mordê-los e desliza por ela. Infelizmente, há uma rachadura na pedra, que atinge Shrek bem na virilha. Seus olhos se cruzam e, ao chegar ao fundo do escorregador, ele geme e tropeça. Dragon os persegue, a corrente do lustre ainda se desfazendo. Eles são perseguidos por Dragon por um grande salão, sua corrente se enrolando em vários pilares de pedra enquanto Shrek ziguezagueia ao redor deles. Dragon acaba na frente deles e cospe fogo. Shrek desvia do fogo e foge, saltando sobre várias fileiras de correntes. Ele para)

# Shrek: Certo, vocês dois, vão para a saída! (colocando Burro e Fiona no chão) Eu cuido do dragão.

# (Shrek agarra uma espada presa no chão e a enfia em um elo da corrente, bem fundo no chão. Shrek alcança Burro e Fiona, que estão esperando perto da saída)

# Shrek: Corra!

# (Eles correm o mais rápido que podem para fora do castelo e para a ponte frágil enquanto Dragão cospe uma enorme bola de fogo atrás deles. Quando chegam ao meio da ponte, o fogo queima a ponte, que se quebra ao meio. Eles se penduram na ponte enquanto são balançados para o outro lado. Burro, incapaz de se agarrar, cai, mas Shrek o segura pela perna. Fiona grita de horror quando Dragão voa sobre a lava fervente para pegá-los. De repente, o lustre puxa Dragão de volta, a espada tendo se alojado em uma coluna de pedra e prendendo a corrente. O grupo rapidamente sobe para a segurança. Dragão solta um rugido derrotado e então dá um gemido triste)

# VULCÃO - EXTERIOR
# (A primeira a sair, Fiona desliza graciosamente até o sopé da colina do vulcão)

# Fiona: Você conseguiu! Você me resgatou! Você é incrível.

# Atrás dela, o burro desce a colina rolando.

# Fiona: Você é... você é maravilhosa. Você é...

# (ela se vira para ver Shrek deslizando morro abaixo e colidindo com Burro)

# Fiona: Um pouco heterodoxo, admito. Mas... teu feito é grandioso, e teu coração é puro. Estou eternamente em dívida contigo.

# Burro: Ahem...

# Fiona: E onde estaria um bravo cavaleiro sem seu nobre corcel?

# (ela se abaixa, apertando o rosto do Burro)

# Burro: Espero que tenha ouvido. Ela me chamou de corcel nobre. Ela acha que eu sou um corcel.

# (Burro fica vermelho, fazendo Fiona rir e Shrek revirar os olhos)

# Fiona: A batalha foi vencida. Pode tirar o capacete, bom cavaleiro.

# (Burro engasga e faz contato visual com Shrek)

# Shrek: Não, não.

# Fiona: Por que não?

# Shrek: Eu...eu tenho cabelo de capacete.

# Fiona: Por favor. Eu gostaria de olhar para o rosto do meu salvador.

# Shrek: Ah, não, você não faria isso.

# Fiona: Mas como você vai me beijar?

# Shrek: O quê?

# (Shrek recua e bate na parede)

# Shrek: (para Burro) Isso não estava na descrição do trabalho.

# Burro: Talvez seja uma vantagem! (levanta as sobrancelhas sugestivamente)

# Fiona: Não, é o destino. Ah, você deve saber como é: uma princesa presa em uma torre e atacada por um dragão é resgatada por um bravo cavaleiro, e então eles compartilham o primeiro beijo do amor verdadeiro.

# (Ambos lançam olhares arregalados para Fiona)

# Burro: Hmm? Com ​​o Shrek? Você pensa... quem, uau, espera um segundo. Você acha que o Shrek é o seu verdadeiro amor?

# Fiona: Bem... sim.

# (Fiona sorri timidamente para Shrek. Shrek e Burro se viram um para o outro e começam a rir)

# Burro: Você acha que Shrek é seu verdadeiro amor!

# Fiona: (irritada) O que é tão engraçado?

# Shrek: Digamos que eu não sou seu tipo, ok?

# Fiona: Claro que sim. Você é minha salvadora. Agora... agora tire o capacete.

# Shrek: Olha. Eu realmente não acho que isso seja uma boa ideia.

# Fiona: Apenas tire o capacete.

# Shrek: Eu não vou.

# Fiona: Tire isso.

# Shrek: Não!

# Fiona: (Grita) AGORA!

# Shrek: CERTO! Calma! Como ordenar, Alteza.

# (Shrek balança a cabeça, tira o capacete e revela seu lado ogro. Fiona olha para ele sem expressão, confusa, mas não assustada. Shrek sorri sem jeito)

# Fiona: Você é...um ogro.

# Shrek: Ah, você estava esperando o Príncipe Encantado ?

# Fiona: Bem... sim, na verdade! Ah, não. Isso está tudo errado. Você não deveria ser um ogro! (sai andando)

# Shrek: (suspira) Princesa, fui enviado para resgatá-la pelo Lorde Farquaad, ok? É ele quem quer se casar com você.

# (a menção deste Lorde Farquaad faz Fiona se virar surpresa)

# Fiona: Então por que ele não veio me resgatar?

# Shrek: Boa pergunta. Você deveria perguntar isso a ele quando chegarmos lá.

# (Shrek se vira e zomba de Fiona enquanto remove a pouca armadura que ainda resta presa a ele)

# Fiona: Mas eu preciso ser resgatada pelo meu verdadeiro amor! Não por um ogro e oi...oi...seu bichinho de estimação.

# Burro: Bem, isso é tudo para um nobre corcel.

# Shrek: Olha, princesa, você não está facilitando meu trabalho.

# Fiona: Bem, sinto muito, mas seu trabalho não é problema meu. Pode dizer ao Lorde "Farquaad" que, se ele quiser me resgatar de verdade, estarei esperando por ele aqui mesmo.

# (Fiona senta-se determinadamente em uma rocha próxima)

# Shrek: Ei! Eu não sou o mensageiro de ninguém, tá? (Avançando em direção a ela) Eu sou um entregador.

# Fiona: Você não ousaria.

# (Shrek pega Fiona e a coloca sobre o ombro)

# Fiona: (grita) Me coloque no chão!

# Shrek: Você vem, Burro?

# Burro: Ah, sim! Estou logo atrás de você.

# (Fiona agora está chutando e gritando)

# Fiona: Me solte ou você vai sofrer as consequências! Isso não é digno! Me solte!

# (Fiona dá um tapa na nuca de Shrek e grita de frustração)

# BOSQUES
# (Horas se passaram e Fiona se acalmou. Ela fica pendurada, mole, enquanto Shrek a carrega e Burro caminha atrás deles)

# Burro: Certo, então aqui vai outra pergunta. Digamos que haja uma mulher que te agrade, mas você não gosta dela desse jeito. Como você a decepciona facilmente, sem magoá-la, mas sem te queimar e te devorar? Como você faz isso?

# Fiona: Diga a ela que ela não é o seu verdadeiro amor. Todo mundo sabe o que acontece quando você encontra o seu...

# (Shrek a interrompe com um reajuste deliberado e saltitante)

# Fiona: Ei! Quanto mais cedo chegarmos a Duloc, melhor.

# Burro: Ah, você vai adorar lá, princesa. É lindo!

# Fiona: E quanto ao meu futuro noivo? Lorde Farquaad? Como ele é?

# Shrek: Bem, deixe-me colocar desta forma, princesa.

# (Shrek joga Fiona no chão sem cerimônia e vai até um lago próximo para se lavar)

# Shrek: Homens do nível de Farquaad são..." escassos" .

# (ele ri e o Burro se junta a ele)

# Burro: Não sei, Shrek. Há quem pense " pouco" dele.

# (Eles riem ainda mais alto)

# Fiona: Parem com isso. Parem com isso, vocês dois. Vocês só estão com inveja porque nunca conseguirão se comparar a um grande governante como Lorde Farquaad.

# Shrek: É, talvez você tenha razão, princesa. Mas eu vou deixar você fazer a " medição"... quando você o vir amanhã.

# Fiona: Amanhã?

# (Em pânico, Fiona olha para trás com medo para o pôr do sol)

# Fiona: Vai demorar tanto assim? Não deveríamos parar para acampar?

# Shrek: Não, isso vai demorar mais. Podemos continuar.

# Fiona: Mas há... ladrões na floresta.

# Burro: Uau! Tempo esgotado, Shrek! O acampamento está definitivamente começando a soar bem.

# Shrek: Ei, vamos lá. Eu sou mais assustador do que qualquer coisa que veremos nesta floresta.

# (Fiona pula na frente de Shrek, bloqueando-o)

# Fiona: (Gritando) PRECISO ENCONTRAR UM LUGAR PARA ACAMPAR AGORA!!

# (Shrek e Burro abaixam as orelhas, surpresos com a explosão dela)

# PENHASCO
# (Poucos minutos depois, Shrek está rolando uma grande pedra para longe da boca de uma caverna)

# Shrek: Ei! Aqui!

# Burro: Shrek, podemos fazer melhor que isso. Não acho que isso seja digno de uma princesa.

# (Fiona desvia sua atenção do pôr do sol)

# Fiona: Não, não, está perfeito. Só precisa de alguns toques caseiros.

# Shrek: Toques caseiros? Tipo o quê?

# (Ele ouve um enorme som de algo se rasgando e olha para Fiona, que arrancou a casca de uma árvore com as próprias mãos)

# Fiona: Uma porta. Bem, senhores, desejo-lhes boa noite.

# (Ela entra na caverna e coloca a porta de casca atrás dela)

# Burro: Você quer que eu vá aí e leia uma história para você dormir? Porque eu vou.

# Fiona: EU DISSE BOA NOITE!

# (Shrek olha para o Burro por um segundo e então estende a mão para mover a pedra de volta para a frente da entrada)

# Burro: Shrek, o que você está fazendo?!

# Shrek: (risos) Eu só... sabe... Ah, qual é. Eu só estava brincando.

# PENHASCO - NOITE
# (Mais tarde naquela noite, Shrek e Burro estão sentados ao redor de uma fogueira. Eles olham para o céu enquanto Shrek aponta certas constelações de estrelas para Burro)

# Shrek: E, uh, aquele, esse é o Throwback, o único ogro que já cuspiu em três campos de trigo.

# Burro: Certo. É. Ei, você consegue prever meu futuro com base nessas estrelas?

# Shrek: As estrelas não predizem o futuro, Burro. Elas contam histórias. Olha, lá está o Bloodnut, o Flatulento . Você já deve ter adivinhado por que ele é famoso. (risos)

# Burro: Tudo bem, agora eu sei que você está inventando isso.

# Shrek: Não, olha.

# (Shrek traça a constelação com o dedo)

# Shrek: Lá está ele, e lá está o grupo de caçadores fugindo do seu fedor.

# Burro: Cara, isso não passa de um monte de pontinhos.

# Shrek: Sabe, Burro, às vezes as coisas são mais do que parecem. Hum?

# (Shrek olha para ver se Burro o entendeu, mas recebe um olhar vazio)

# Shrek: Esqueça.

# Burro: Ei, Shrek, o que faremos quando tivermos nosso pântano?

# Shrek: Nosso pântano?

# Burro: Sabe, quando terminarmos de resgatar a princesa e tudo mais.

# Shrek: Nós ? Burro, não existe nós . Não existe nosso . Somos só eu e meu pântano. E a primeira coisa que vou fazer é construir um muro de três metros ao redor da minha terra.

# (Ele vira as costas para o Burro)

# Burro: Você me machucou profundamente, Shrek. Você me machucou profundamente agora mesmo.

# (Burro caminha até encarar Shrek)

# Burro: Sabe o que eu acho? Acho que essa coisa toda de muro é só uma forma de manter alguém longe.

# Shrek: Não, você acha?

# (Shrek se vira novamente)

# Burro: Você está escondendo alguma coisa?

# Shrek: Não se preocupe, Burro.

# (Ele deita de costas. O burro se inclina sobre ele)

# Burro: Ah, essa é mais uma daquelas coisas de cebola, não é?

# Shrek: Não, essa é uma daquelas coisas do tipo "deixa pra lá e deixa pra lá"!

# Burro: Por que você não quer falar sobre isso?

# Shrek: Por que você quer falar sobre isso? (vira-se)

# Burro: Por que você está bloqueando?

# Shrek: Eu não estou bloqueando! (vira)

# Burro: Ah, sim, você é.

# Shrek: Burro, estou te avisando...

# Burro: Quem você está tentando manter fora?

# (Shrek se levanta e encara o Burro)

# Shrek: (Gritando com o Burro) TODO MUNDO! TUDO BEM?!

# Burro: Ah, agora estamos chegando a algum lugar.

# (Sem que nenhum deles fosse visto, Fiona estava espiando pela porta da caverna, escutando a conversa)

# Shrek: Ah! Pelo amor de Deus!

# (Shrek caminha até a beira do penhasco e se senta)

# Burro: Ei, qual é o seu problema, Shrek? Afinal, o que você tem contra o mundo inteiro?

# Shrek: Olha, eu não sou o único com o problema, ok? É o mundo que parece ter um problema comigo ! As pessoas olham para mim e dizem: "Aah! Socorro! Corra! Um ogro grande, estúpido e feio!" ( deprimido ). Elas me julgam antes mesmo de me conhecerem. É por isso que estou melhor sozinho.

# (Escondido nas sombras da caverna, os olhos de Fiona eram simpáticos. Ela fecha a porta. Burro encara Shrek em silêncio por um momento e então se senta ao lado dele)

# Burro: Sabe de uma coisa? Quando nos conhecemos, não achei que você fosse só um ogro grande, idiota e feio.

# Shrek: Sim, eu sei.

# Burro: Então, tem algum burro aí em cima?

# Shrek: Bem, tem, hum, Gabby... a Pequena... e Irritante.

# Burro: Certo, certo, agora entendi. Aquele grande e brilhante, ali. Aquele ali?

# Shrek: Essa é a lua.

# Burro: Ah, tudo bem.

# DULOC - QUARTO DO LORD FARQUAAD
# (O quarto de Lorde Farquaad está cheio de itens preparados para seu casamento, incluindo coroas e trajes de casamento para ele e Fiona. A Mamãe Ursa agora é um tapete empalhado. Uma música suave toca ao fundo. Lorde Farquaad está deitado na cama com o Espelho Mágico colocado aos pés da cama)

# Lord Farquaad: Mais uma vez, mostre-me novamente.

# (Ouvimos o som da fita sendo rebobinada.)

# Lorde Farquaad: Espelho, espelho meu, mostre-a para mim. Mostre-me a princesa.

# Espelho Mágico: (desconfortavelmente) Hmm.

# (O Espelho rebobina relutantemente e começa a tocar novamente desde o início, exibindo a imagem de Fiona esperando em sua torre)

# Lorde Farquaad: Ah...perfeito.

# Lorde Farquaad olha para baixo e puxa o lençol para se cobrir enquanto as cobertas sobem.

# PENHASCO - MANHÃ
# (Fiona sai da caverna e olha para Shrek e Burro, que ainda estão dormindo. Ela vagueia pela floresta, maravilhada com a natureza, e começa a cantar. Um pássaro azul voa para se juntar à sua canção. Ela atinge notas cada vez mais altas e o pássaro se esforça para acompanhá-la. Fiona atinge uma nota alta e horrível que faz o pássaro explodir. Fiona parece culpada pelo que fez com ele, mas olha para os ovos que o pássaro deixou para trás. Um pouco mais tarde, Fiona está fritando os ovos na fogueira usando uma frigideira de pedra. Shrek acorda, sente o cheiro da comida e nota Fiona. Burro está falando sozinho enquanto dorme)

# Burro: Mmm, é, você sabe que eu gosto assim. Vamos, querida. Eu disse que gosto...

# Shrek: Burro, acorde. (sacude-o)

# Burro: Hein? O quê?

# Shrek: Acorde.

# Burro: O quê? (se espreguiça e boceja)

# Fiona: Bom dia. Hum... como você gosta dos seus ovos?

# Burro: Oh, bom dia, princesa!

# Shrek: O que é tudo isso?

# Fiona: Sabe, a gente começou meio mal ontem e eu queria te compensar. Afinal, você me salvou.

# (Fiona se levanta e coloca os ovos na frente deles)

# Shrek: Ah, obrigado.

# (O burro cheira os ovos e lambe os lábios)

# Fiona: Bom, comam. Temos um grande dia pela frente.

# (Fiona vai embora, aparentemente de melhor humor do que ontem. Shrek e Burro se entreolham)

# FLORESTA DE SHERWOOD
# (Os três continuam sua jornada de volta para Duloc pela floresta. Shrek solta um arroto alto)

# Burro: Shrek!

# Shrek: O quê? É um elogio. É melhor fora do que dentro, eu sempre digo. (risos)

# Burro: Bem, isso não é jeito de se comportar na frente de uma princesa!

# (Fiona arrota, parando Shrek e Burro no meio do caminho)

# Fiona: Obrigada.

# Burro: Ela é tão desagradável quanto você.

# Shrek: (risos) Sabe, você não é exatamente o que eu esperava.

# Fiona: Bem, talvez você não devesse julgar as pessoas antes de conhecê-las.

# (Ela sorri e continua andando, cantando baixinho. De repente, do nada, um homem desce e leva Fiona embora)

# Monsieur Hood: La liberté! Ei!

# SHREK: Princesa!

# (Fiona e o homem desconhecido pousam em um galho bem alto nas árvores. Não é outro senão Robin Hood , também conhecido como Robin Hood. Fiona se desvencilha do Monsieur Hood, que tem a mão em volta da cintura dela)

# Fiona: Ah! Espera, espera... o que você está fazendo?!

# Monsieur Hood: Fique quieto, mon chérie , pois eu sou o seu salvador! E eu estou resgatando você deste verde...

# (Monsieur Hood leva a mão de Fiona ao peito e então cobre os braços de Fiona com beijos enquanto ela se afasta com desgosto)

# Monsieur Hood: ...fera.

# (Seu sorriso só é recebido com aborrecimento, o que o confunde)

# Shrek: Ei! Essa é a minha princesa! Vá procurar a sua!

# Monsieur Hood: Por favor, monstro! Não vê que estou um pouco ocupado?

# (Fiona dá um empurrão com uma mão em Monsieur Hood e enfia o dedo em seu peito)

# Fiona: Olha, amigo, eu não sei quem você pensa que é!

# Monsieur Hood: Ah! Claro! Que grosseria! Por favor, deixe-me apresentar.

# Ele junta a mão e chama para a floresta

# Monsieur Hood: Oh, homens alegres! (risos)

# (De repente, um acordeão começa a tocar e os Merrymen saem dos arbustos. Eles começam a cantar junto com Monsieur Hood)

# Merrymen: Ta, dah, dah, dah, uau.

# Monsieur Hood: (Dá uma maçã ao Burro) Eu roubo dos ricos e dou aos necessitados.

# Merryman: Ele pega uma pequena porcentagem,

# Monsieur Hood: Mas eu não sou ganancioso. Eu resgato donzelas bonitas, cara, eu sou bom.

# Merrymen: Que cara, Monsieur Hood.

# Monsieur Hood: Vamos lá. (Dança irlandesa) Eu gosto de uma briga honesta e de uma donzela atrevida...

# Merrymen: O que ele está basicamente dizendo é que gosta de...

# Monsieur Hood: Pago! Então... (Merrymen virou estrela) Quando um ogro no mato agarra uma moça pelo bumbum. Isso é ruim.

# Merrymen: Isso é ruim. Isso é ruim. Isso é ruim!

# Monsieur Hood: Quando uma bela está com uma fera, isso me deixa terrivelmente furioso!

# Merrymen: Ele está bravo, ele está muito, muito bravo!

# (Fiona, ainda em cima da árvore, olha para baixo. Sua expressão muda de confusão para horror quando Monsieur Hood canta o último verso)

# Monsieur Hood: Vou pegar minha lâmina e enfiá-la no seu coração, fiquem de olho em mim, rapazes, porque estou prestes a começar...

# (Fiona desce do galho da árvore e chuta Monsieur Hood na cabeça, deixando-o inconsciente. Ela cai com um mortal para trás na frente de Shrek e Burro)

# Fiona: Cara, isso foi irritante!

# (Shrek olha para ela com admiração)

# Merryman: Oh, seu pequeno--

# (O Homem Feliz atira uma flecha em Fiona, que corajosamente se esquiva. A flecha passa voando por ela e vai em direção ao Burro, que pula nos braços de Shrek para sair do caminho. Fiona demonstra suas habilidades em artes marciais e derrota facilmente todos os Homens Felizes. Os Homens Felizes são deixados no chão e Fiona vai embora. Fiona parece um pouco envergonhada enquanto alisa seu vestido e recupera a compostura.)

# Fiona: Uh, vamos?

# Shrek: Segure o telefone.

# (Pego de surpresa, Shrek larga o Burro e começa a andar atrás de Fiona)

# Shrek: Oh! Uau, uau, uau. Espera aí. De onde veio isso?

# Fiona: O quê?

# Shrek: Isso! Lá atrás. Foi incrível! Onde você aprendeu isso?

# (Fiona cora)

# FIONA: Bem...(risos) quando se vive sozinho, é preciso aprender essas coisas, caso haja uma... haja uma flecha na sua bunda!

# (Fiona aponta para baixo, para uma pequena flecha saindo da bunda de Shrek)

# Shrek: O quê? Ah, olha só isso?

# Fiona: Ah, não. A culpa é toda minha. Sinto muito.

# (Shrek puxa levemente a flecha, mas para, estremecendo de dor. Burro os alcança)

# Burro: Por quê? O que houve?

# Fiona: Shrek está ferido.

# Burro: O Shrek está ferido! O Shrek está ferido?!

# (O burro começa a correr freneticamente)

# Burro: Ah, não, o Shrek vai morrer!

# Shrek: Burro, estou bem.

# Burro: Você não pode fazer isso comigo, Shrek. Sou jovem demais para você morrer! Mantenha as pernas elevadas! Vire a cabeça e tussa! Alguém conhece o Heimlich?!

# (Fiona agarra a cabeça do Burro e a puxa para baixo em sua direção)

# Fiona: Burro! Calma! Se quiser ajudar o Shrek, corra para a floresta e encontre para mim uma flor azul com espinhos vermelhos.

# Burro: Flor azul, espinhos vermelhos. Certo, estou cuidando disso. Flor azul, espinhos vermelhos. Não morra, Shrek.

# (O burro começa a seguir em uma direção aleatória em direção à floresta.)

# Burro: E se você vir um túnel longo, fique longe da luz !

# Shrek e Fiona: Burro!

# Burro: Ah, sim. Certo. Flor azul, espinhos vermelhos. Flor azul, espinhos vermelhos...

# (O burro sai marchando, ainda cantando, até ficar fora do alcance da voz)

# Shrek: Para que servem as flores?

# Fiona: Por se livrar do Burro.

# Shrek: Ah...

# (O olhar confuso de Shrek se transforma em um grande sorriso)

# Fiona: Agora fique quieta que eu vou arrancar essa coisa.

# Fiona agarra a flecha e começa a puxá-la. Shrek estremece e salta para longe.

# Shrek: Ai! Ei! Calma com os puxões!

# Fiona: Bem, me desculpe, mas isso tem que sair.

# Shrek: Não, é macio.

# (Enquanto eles continuam conversando, Fiona continua tentando agarrar a flecha enquanto Shrek desvia de suas tentativas)

# Fiona: Agora, fique parada.

# Shrek: O que você está fazendo é o oposto de ajudar.

# Fiona: Não se mova.

# Shrek: Olha, tempo limite.

# (Shrek coloca a mão inteira sobre o rosto de Fiona, parando-a no meio do caminho)

# Fiona: Você poderia...

# (Ela tira a mão de Shrek do rosto)

# Fiona: Certo. O que você propõe que façamos?

# FLORESTA DE SHERWOOD - OUTROS LUGARES
# (Mais fundo na floresta, o Burro procura apressadamente a flor)

# Burro: Flor azul, espinhos vermelhos. Flor azul, espinhos vermelhos. Flor azul, espinhos vermelhos. Isso seria muito mais fácil se eu não fosse daltônico! Flor azul, espinhos vermelhos.

# (De repente ele ouve um grito distante de Shrek)

# Shrek: Owww!

# Burro: Calma aí, Shrek! Já vou!

# (O burro arranca uma flor de um arbusto próximo, que por acaso é uma flor azul com espinhos vermelhos, e sai correndo)

# FLORESTA DE SHERWOOD - CLAREIRA
# (De volta à clareira, Shrek está deitado no chão de bruços, enquanto Fiona fica em pé sobre ele, usando as duas mãos para tentar remover a flecha)

# Shrek: Ai! Não é bom.

# Fiona: Certo. N--Certo. Eu quase consigo ver... É quase...

# Shrek: Ai! Ohh!

# (Ele rola, derrubando Fiona e fazendo-a cair em cima dele. Por um momento, eles se encaram.)

# Burro: Ahem.

# (Ambos se assustam com a interrupção do Burro. O Burro, com a flor caída a seus pés, lança-lhes um olhar sugestivo)

# Shrek: Não aconteceu nada.

# (Shrek empurra Fiona para longe dele e rola para encarar o Burro)

# Shrek: Nós estávamos apenas, uh...

# Burro: Olha, se você quisesse ficar sozinho, tudo o que você tinha que fazer era pedir, ok?

# Shrek: Ah, qual é! É a última coisa que me passa pela cabeça. A princesa aqui estava apenas...

# (Fiona rapidamente puxa a flecha da bunda de Shrek com um grande puxão)

# SHREK: Arghhh!

# (Ele se vira para olhar para Fiona, que balança a flecha de um lado para o outro de brincadeira com um sorriso tímido)

# Shrek: Ai!

# Burro: Ei, o que é isso? (rindo) Isso é... isso é sangue?

# (O burro desmaia e cai em uma pilha de folhas. Shrek o pega e o joga por cima do ombro, e os três continuam sua jornada. Há uma montagem de cenas enquanto o grupo retorna para Duloc)

# (O grupo chega a um rio sem caminho, embora seja claramente raso o suficiente para atravessar a pé. Shrek sobe no topo de uma árvore, usando seu peso para fazer com que a árvore se curve sobre o rio e forme uma ponte. Fiona atravessa primeiro e coloca a mão nas costas de Shrek quando chega ao outro lado. Shrek sorri e se levanta enquanto Burro ainda está atravessando, lançando-o de volta para o outro lado. Em um campo, Shrek afasta um enxame de moscas que o seguem. Fiona pega uma teia de aranha próxima de um galho de árvore e corre pelo campo, balançando-a para pegar os insetos. Ela gira o galho para formar uma espécie de algodão-doce e o entrega a Shrek como um agrado. Enquanto ele se afasta mordendo-o, Urgh! ela lambe os dedos. Shrek pega um sapo e o enche como um balão para dar a Fiona. Fiona pega uma cobra, sopra em sua boca, a transforma em um animal de balão e o apresenta a Shrek. Fiona começa uma brincadeira de empurrões com Shrek, que acaba jogando-a nos arbustos. Ela joga um galho nele enquanto ambos riem, largando seus balões. O Burro pula atrás deles.

# MOINHO DE VENTO - EXTERIOR
# (Depois de sair da floresta, o grupo chega a uma pequena elevação onde se ergue um antigo moinho de vento em ruínas. Os campos de Duloc se estendem à frente, e mais ao longe fica o Castelo de Duloc)

# Shrek: Aí está, princesa. Seu futuro a aguarda.

# Fiona: Esse é o Duloc?

# (Fiona fica de pé com o braço sobre o de Shrek, mas Burro se coloca entre eles. Ambos dão de ombros um para o outro)

# Burro: É, eu sei. Sabe, o Shrek acha que o Lorde Farquaad está compensando alguma coisa, o que eu acho que significa que ele tem um...

# (Shrek interrompe Burro pisando em seu pé, fazendo-o cair no chão de dor. Fiona lança um olhar desconfiado para Shrek)

# Burro: Ai!

# Shrek: Hum, eu, uh... Acho melhor seguirmos em frente.

# Fiona: Claro. Mas, Shrek? Eu estou preocupada com o Burro.

# Shrek: O quê?

# Fiona: Olha só ele. Ele não parece estar nada bem.

# (Parece que não há nada de errado com o Burro. Shrek sorri com conhecimento de causa para Fiona)

# Burro: Do ​​que você está falando? Estou bem.

# (Fiona se ajoelha e pega a cabeça do Burro em seus braços)

# Fiona: Bom, é o que sempre dizem, e então... então... então, a próxima coisa que você sabe é que está de costas. Morto.

# Shrek: Sabe, ela tem razão. Você está horrível. Quer se sentar?

# Fiona: Sabe, vou fazer um chá para você.

# Burro: Eu não queria dizer nada, mas senti uma pontada no pescoço, e quando viro a cabeça assim, olha.

# (O burro inclina bruscamente a cabeça para o lado, emitindo um estalo alto)

# Burro: Ai! Viu?

# (Shrek e Fiona trocam olhares felizes, tendo inventado uma desculpa para ganhar tempo)

# Shrek: Quem está com fome? Vou encontrar algo para jantar.

# Fiona: Vou pegar a lenha.

# (Shrek e Fiona caminham em direções diferentes)

# Burro: Ei, aonde você vai? Nossa, não sinto meus dedos! (olha para baixo) Não tenho dedos! Acho que preciso de um abraço.

# MOINHO DE VENTO - EXTERIOR - NOITE
# (Shrek acendeu uma fogueira e está cozinhando algo no espeto enquanto Fiona come).

# Fiona: Hum. Isso é bom. Isso é muito bom. O que é isso?

# Shrek: Uh, rato de maconha. Estilo espeto rotativo.

# Fiona: Sério. Que delícia!

# Shrek: Bom, elas também ficam ótimas em ensopados. Não quero me gabar, mas eu faço um ensopado de rato-da-erva daninha incrível.

# (Fiona sorri, mas o sorriso desaparece rapidamente quando ela olha para Duloc à distância)

# Fiona: Acho que vou jantar um pouco diferente amanhã à noite.

# Shrek: Talvez você possa me visitar no pântano um dia desses. Eu cozinho todo tipo de coisa para você. Sopa de sapo-do-pântano, tártaro de olho de peixe... o que você quiser.

# (Fiona agora está olhando atentamente para Shrek, sorrindo)

# Fiona: Hmmm, eu adoraria.

# (Eles olham nos olhos um do outro com desejo)

# Shrek: Hum...princesa?

# FIONA: Sim...Shrek?

# Shrek: Eu, hum, eu estava pensando... você... (suspira) Você vai comer isso?

# (Shrek aponta para seu último pedaço de comida. Fiona, esperando uma pergunta diferente, remove o rato-da-erva enquanto Shrek fica irritado com as palavras que não conseguem sair. Quando Fiona o entrega a Shrek, ele agarra a mão dela. Os dois se inclinam lentamente um em direção ao outro. Burro interrompe o momento)

# Burro: Cara, isso não é romântico? Olha só o pôr do sol.

# (Shrek e Fiona são tirados do momento. O humor de Fiona muda e ela se senta abruptamente para encarar o pôr do sol)

# Fiona: Pôr do sol?! Ah, não! Quer dizer, já está tarde. E-está muito tarde.

# (Ela começa a recuar em direção ao moinho de vento)

# Shrek: O quê?

# Burro: Espere um minuto. Já entendi o que está acontecendo.

# (Fiona olha para Burro e congela de pânico)

# Burro: Você tem medo do escuro, não é?

# Fiona: Sim! Sim, é isso mesmo. Estou apavorada. Sabe, é melhor eu entrar.

# (Ela sorri enquanto se vira para subir os degraus do moinho de vento. Ela dá um suspiro de alívio)

# Burro: Não se sinta mal, princesa. Eu também tinha medo do escuro, até... Ei, não, espera. Eu ainda tenho medo do escuro.

# (Shrek geme e Fiona ri)

# Fiona: Boa noite.

# Shrek: Boa noite.

# (Fiona entra no moinho de vento, lança um olhar para Shrek e fecha a porta. Burro olha para Shrek com um novo olhar)

# Burro: Ah! Agora eu realmente entendi o que está acontecendo aqui.

# Shrek: Ah, do que você está falando?

# (O burro trota até Shrek enquanto ele se ajoelha perto do fogo e brinca com um dos espetos)

# Burro: Eu nem quero ouvir. Olha, eu sou um animal e tenho instintos. E eu sei que vocês dois estavam se pegando. Eu podia sentir.

# Shrek: Você está louco. Vou levá-la de volta para Farquaad.

# Burro: Ah, vamos lá, Shrek. Acorde e sinta o cheiro dos feromônios. Entre e diga a ela como você se sente.

# Shrek: Eu... não há nada a dizer. Além disso, mesmo que eu contasse isso a ela, bem, você sabe... e não estou dizendo que conto, porque eu não conto... ela é uma princesa, e eu...

# Burro: Um ogro?

# Shrek: Sim. Um ogro.

# (Shrek joga o cuspe de lado e vai embora)

# Burro: Ei, onde você vai?

# Shrek: Para conseguir...mais lenha.

# (Burro olha desconfiado para a grande pilha de lenha já empilhada. Shrek senta-se na colina e observa Duloc até o anoitecer)

# MOINHO DE VENTO - EXTERIOR - NOITE
# (O burro abre a porta do moinho de vento e entra. O moinho abandonado está cheio de sombras e teias de aranha. Tudo está quieto e Fiona não está em lugar nenhum)

# Burro: Princesa? Princesa Fiona? Princesa, onde você está?

# (Um grupo de pássaros voa em bando do topo do telhado, assustando Burro. Ele continua).

# Burro: Princesa?

# (Uma mão agarra os degraus de uma escada)

# Burro: Está muito assustador aqui dentro. Não estou brincando.

# (Fiona olha para o Burro, envolto em sombras, de cima de uma plataforma. Ela tenta escapar, mas falha quando uma tábua de madeira quebra e a faz cair com um estrondo. Ela grita e pousa em um saco de farinha, lançando uma nuvem de farinha no ar. O Burro fica paralisado de medo, incapaz de dizer quem é a figura)

# Burro: Aah!

# Fiona: Ah, não!

# Burro: Não, não, socorro!

# (Uma ogra emerge da nuvem de farinha, aproximando-se do Burro)

# Burro: Shrek! Shrek! Shrek!

# Fiona: Não, está tudo bem! Está tudo bem!

# Burro: O que você fez com a princesa?!

# Fiona: Burro! Eu sou a princesa.

# Burro: Aah!

# Fiona: Sou eu, neste corpo.

# Burro: Meu Deus! Você comeu a princesa! (para o estômago dela) Você consegue me ouvir?

# Fiona: Burro!

# Burro: (ainda apontando para a barriga) Escuta, continua respirando! Eu vou te tirar daí!

# Fiona: Não!

# Burro: Shrek! Shrek! Shrek!

# Fiona: (Cobrindo a boca do Burro e fazendo-o ficar quieto para acalmá-lo)

# Burro: (Abafado) Shrek! Shrek! Shrek...

# Fiona: Sou eu.

# (O burro olha em seus olhos enquanto ela acaricia seu focinho e o acalma)

# Burro: Princesa...? O que aconteceu com você? Você está, uh... uh... eh... diferente.

# Fiona: Eu sou feia, ok?

# Burro: Pois é! Foi algo que você comeu? Porque eu disse ao Shrek que aqueles ratos eram uma má ideia. Você é o que você come, eu disse. Agora...

# Fiona: Não! Eu... eu sou assim desde que me lembro.

# Burro: Como assim? Olha, eu nunca te vi assim antes.

# Fiona: Isso só acontece quando o sol se põe.

# (Fiona se inclina sobre um barril cheio de água, olhando para seu reflexo)

# Fiona: "De noite, de um jeito, de dia, de outro. Essa será a norma... até você encontrar o primeiro beijo do amor verdadeiro... e então assumir a verdadeira forma do amor."

# Burro: Nossa, que lindo. Eu não sabia que você escrevia poesia.

# Fiona: É um feitiço. (suspiro) Quando eu era pequena, uma bruxa lançou um feitiço em mim. Toda noite eu me transformo nisso. Nessa fera horrível e feia!

# (Fiona bate em seu reflexo na água, que espirra água em Burro)

# Fiona: Fui colocada em uma torre para aguardar o dia em que meu verdadeiro amor me resgataria. É por isso que tenho que me casar com Lorde Farquaad amanhã, antes que o sol se ponha e ele me veja... assim.

# (Ela segura a cabeça e começa a chorar)

# Burro: Tudo bem, tudo bem. Calma. Olha, não é tão ruim assim. Você não é tão feio assim. Bom, ok, não vou mentir. Você é feio. Mas você só fica assim à noite. O Shrek é feio o tempo todo.

# Fiona: Mas, Burro, eu sou uma princesa , e não é assim que uma princesa deve ser.

# Burro: Princesa, que tal se você não se casar com Farquaad?

# Fiona: Eu preciso. Só o beijo do meu verdadeiro amor pode quebrar o feitiço.

# Burro: Mas, sabe, hum... você é meio ogro. E Shrek... bem... vocês têm muito em comum.

# Fiona: Shrek?

# EXTERIOR DO MOINHO DE VENTO
# (Shrek está caminhando em direção ao moinho de vento com um girassol na mão, falando sozinho)

# Shrek: Princesa, eu... uh, como vai, antes de tudo? Bem? Hum, bem para mim também. Estou bem. Vi esta flor e pensei em você porque ela é bonita e... bem, eu não gosto muito dela, mas pensei que você pudesse gostar porque é bonita. Mas eu gosto de você mesmo assim. Eu... uh, uh... (suspira) Estou encrencada. Certo, vamos lá.

# (Ele caminha até a porta e para do lado de fora quando ouve Burro e Fiona conversando)

# Fiona: Não posso me casar com quem eu quiser. Olha bem para mim, Burro. Sério, quem poderia amar uma fera tão horrenda e feia? "Princesa" e "feia" não combinam. É por isso que não posso ficar aqui com o Shrek.

# (Shrek dá um passo para trás em choque, não entendendo o significado da conversa)

# Fiona: Minha única chance de viver feliz para sempre é me casar com meu verdadeiro amor. Não entende, Burro? É assim que tem que ser.

# (Shrek dá um suspiro profundo. Ele joga a flor no chão e vai embora com raiva)

# INTERIOR DO MOINHO DE VENTO
# Fiona: É a única maneira de quebrar o feitiço.

# Burro: Bem, pelo menos você tem que contar a verdade ao Shrek.

# (O burro caminha até a porta)

# Fiona: Não! Você não pode dizer nada. Ninguém pode saber.

# Burro: Qual o sentido de poder falar se você tem que guardar segredos?

# Fiona: Prometa que não vai contar. Prometa!

# Burro: Tudo bem, tudo bem. Não vou contar a ele. Mas você deveria.

# (Burro sai e fala sozinho)

# Burro: Só sei que, antes que isso acabe, vou precisar de muita terapia. Olha só o meu olho tremendo.

# (Fiona abre a porta e o observa se afastar. Ela olha para baixo e vê o girassol deixado perto da porta. Ela o pega e olha ao redor, depois volta para dentro e fecha a porta. O Burro adormece perto do fogo lá fora)

# INTERIOR DO MOINHO DE VENTO - MANHÃ
# (O burro está dormindo. Fiona ainda está acordada, colhendo pétalas do girassol)

# Fiona: Eu digo a ele, eu digo a ele para não fazer isso. Eu digo a ele, eu digo a ele para não fazer isso...

# (Fiona colhe a última pétala do girassol, sorrindo)

# Fiona: Eu digo a ele! Shrek!

# (Ela abre a porta e sai)

# Fiona: Shrek! Tem uma coisa que eu quero...

# (Fiona olha ao redor procurando por Shrek e vê Burro dormindo. Ela vê o sol nascendo e, quando o sol atinge o céu, ela se transforma novamente em humana. Ela olha para cima novamente e vê Shrek vindo em sua direção. Ela corre até ele)

# Fiona: Shrek! Você está bem?

# (Ela coloca a mão no braço dele, mas acidentalmente o provoca quando ele a afasta e passa por ela)

# Shrek: (Sarcasticamente) Perfeito! Nunca esteve melhor.

# Fiona: Eu...eu não...tem uma coisa que preciso te contar.

# Shrek: Não precisa me dizer nada, princesa. Já ouvi o suficiente ontem à noite.

# Fiona: Você ouviu o que eu disse?

# Shrek: Cada palavra.

# (Shrek senta-se nos degraus do moinho de vento e encara Fiona)

# Fiona: Achei que você entenderia.

# Shrek: Ah, entendi. Como você disse: "Quem amaria uma fera horrível e feia?"

# Fiona: Mas pensei que isso não importaria para você.

# Shrek: É? Pois é.

# (Fiona olha para ele em choque, com lágrimas brotando em seus olhos. Shrek olha para além dela e vê um grupo se aproximando)

# Shrek: Ah, bem na hora. Princesa, trouxe uma coisinha para você.

# (Shrek gesticula em direção ao grupo e Fiona fica de boca aberta. Lorde Farquaad chega a cavalo, parecendo mais alto do que o normal, junto com uma escolta de guardas. Burro acorda com um bocejo enquanto os guardas passam marchando)

# Burro: O que eu perdi? O que eu perdi?

# (Um dos guardas se aproxima dele e se prepara para puni-lo enquanto ele começa a correr para longe, murmurando para si mesmo)

# Burro: Quem disse isso? Não pode ter sido um burro.

# (Lord Farquaad para seu cavalo na frente de Fiona)

# Lorde Farquaad: Princesa Fiona.

# Shrek: Como prometido. Agora me entregue.

# Lorde Farquaad: Muito bem, ogro. A escritura do seu pântano está quitada, conforme combinado. Pegue-a e vá embora antes que eu mude de ideia.

# (Shrek arranca a escritura das mãos de um guarda e vai embora. Fiona fica incomodada com a troca de palavras. Ela volta sua atenção para o tão esperado Lorde Farquaad)

# Lorde Farquaad: Perdoe-me, Princesa, por assustá-la, mas você me assustou ... pois eu nunca vi uma beleza tão radiante antes. Eu sou Lorde Farquaad.

# Fiona: Lorde Farquaad? Oh, não, não. Perdoe-me, meu senhor, pois eu estava apenas dizendo uma coisa curta...

# (Lorde Farquaad estala o dedo e é retirado do cavalo pelos guardas. Deixado para trás no cavalo está um grande conjunto de manoplas e um par de extensores de perna que chegam até os estribos, o que o faz parecer tão alto na sela. E colocado na frente dela. Com 1,27 m de altura, ele é muito mais baixo que Fiona. Quando o olhar dela muda de nervosismo para perplexidade, ela sorri sem jeito)

# Fiona: ...adeus.

# Lorde Farquaad: Ah, que fofo! Não precisa desperdiçar boas maneiras com o ogro. Ele não tem sentimentos.

# Fiona: Não, você tem razão. Não importa.

# (Shrek, ainda parado ali perto, de costas, fica magoado com o comentário. Burro observa a conversa com um olhar curioso no rosto)

# Lorde Farquaad: Princesa Fiona, linda, bela e impecável Fiona. Peço sua mão em casamento.

# (Lord Farquaad se ajoelha e pega a mão de Fiona, puxando-a bruscamente para baixo)

# Lorde Farquaad: Você será a noiva perfeita para o noivo perfeito?

# (Fiona faz contato visual com Shrek antes que ele se vire. Seu olhar triste se transforma em amargura)

# Fiona: Lorde Farquaad, eu aceito. Nada faria...

# Lorde Farquaad: Excelente! Vou começar os planos, pois amanhã nos casaremos!

# Fiona: Não!

# (Shrek se vira com um olhar esperançoso no rosto enquanto Fiona tenta recuperar a compostura)

# Fiona: Quer dizer... ah, por que esperar? Vamos nos casar hoje. Antes do pôr do sol.

# (Shrek olha feio e se vira)

# Lorde Farquaad: Ah, estamos ansiosos, não é? Você tem razão. Quanto mais cedo, melhor. Há tanta coisa para fazer!

# (Lorde Farquaad estala os dedos e é erguido sobre seu cavalo por seu guarda. O guarda oferece ajuda a Fiona, mas falha quando ela olha para a sela sozinha)

# Lorde Farquaad: Tem o bufê, o bolo, a banda, a lista de convidados. Capitão, reúna alguns convidados!

# (Fiona, Lorde Farquaad e seus guardas partem em direção a Duloc. Fiona lança um último olhar rancoroso para Shrek)

# Fiona: Adeus, ogro.

# (Burro alcança Shrek enquanto ele se afasta)

# Burro: Shrek, o que você está fazendo? Está deixando ela escapar!

# Shrek: É? E daí?

# Burro: Shrek, tem algo nela que você não sabe. Olha, eu... eu falei com ela ontem à noite... Ela...

# Shrek: É, eu sei que você falou com ela ontem à noite. Vocês são ótimos amigos, não são? Agora, se vocês dois são tão amigos, por que não a seguem até em casa?!

# Burro: Mas Shrek, eu-- eu quero ir com você.

# Shrek: Ei, eu te avisei, não avisei? Você não vai voltar para casa comigo. Eu moro sozinho! Meu pântano! Eu! Mais ninguém! Entendeu? Ninguém! Principalmente burros inúteis, patéticos, irritantes e falantes!

# Burro: Mas, eu pensei...

# Shrek: É, você... sabe de uma coisa? Você pensou errado! (sai furioso)

# Burro: (tristemente) Shrek.

# (Montagem de cenas diferentes. Shrek chega em casa. O pântano está uma bagunça, mas as criaturas de contos de fadas se foram. Fiona está sendo provada para seu vestido de noiva. Shrek joga um girassol na lareira. Lorde Farquaad experimenta orgulhosamente sua coroa. Fiona olha fixamente para seu bolo de casamento, empurrando para baixo uma figura de Lorde Farquaad para mostrar sua altura real. Ela percebe uma armadura que a lembra de Shrek. Burro para perto de um rio onde encontra Dragão chorando, ambos felizes em se verem. Shrek e Fiona tentam jantar, mas começam a chorar)

# PÂNTANO DE SHREK
# (Shrek está sentado à mesa de jantar quando ouve um som lá fora. Ele sai para investigar e vê o Burro reunindo uma fileira de galhos e pequenas pedras)

# Shrek: Burro? O que você está fazendo?

# Burro: Eu acho que, de todas as pessoas, você reconheceria uma parede quando a visse.

# Shrek: Bem, sim. Mas o muro deveria contornar meu pântano, não atravessá-lo.

# Burro: É, mais ou menos a sua metade. Veja, essa é a sua metade, e essa é a minha metade.

# Shrek: Ah! Sua metade? Hum.

# Burro: Sim, minha metade. Ajudei a resgatar a princesa. Fiz metade do trabalho. Fico com metade do saque. Agora me passa aquela pedra grande, aquela que parece a sua cabeça.

# (Shrek começa a derrubar o muro e pega um galho grande. Burro bate a cabeça nele e os dois lutam por ele)

# Shrek: Afaste-se!

# Burro: Não, recue você .

# Shrek: Este é o meu pântano!

# Burro: Nosso pântano!

# Shrek: Solte, Burro!

# Burro: Você me solta!

# Shrek: Idiota teimoso!

# Burro: Ogro fedorento.

# Shrek: Ótimo!

# (Shrek de repente solta o galho, fazendo o Burro tropeçar, e vai embora)

# Burro: Ei, ei, volta aqui. Ainda não terminei com você.

# Shrek: Bem, terminei com você!

# (O burro começa a segui-lo)

# Burro: Uh-uh! Sabe, com você é sempre "eu, eu, eu!" Bem, adivinha! Agora é a minha vez! Então, cale a boca e preste atenção!

# (Assim que Shrek se aproxima da porta de sua casa, Burro pula na frente dele. Shrek caminha em outra direção)

# Burro: Você é mau comigo, me insulta e não dá valor a nada do que eu faço! Você está sempre me empurrando ou me afastando.

# Shrek: Ah, é? Bom, se eu te tratei tão mal, por que você voltou?

# Burro: Porque é isso que os amigos fazem! Eles perdoam uns aos outros!

# Shrek: Ah, sim. Você tem razão, Burro. Eu te perdoo... POR ME ESFAQUEAR PELAS COSTAS!

# (Shrek entra na latrina e bate a porta atrás de si)

# Burro: Ohhhhh! Você está tão enrolado em camadas, garoto cebola, que tem medo dos seus próprios sentimentos.

# Shrek: Vá embora!

# Burro: Viu! Lá está você, fazendo de novo, igualzinho ao que fez com a Fiona. E tudo o que ela fez foi gostar de você, talvez até te amar.

# Shrek: Me ama?! Ela disse que eu era feio! Uma criatura horrível! Ouvi vocês dois conversando.

# Burro: Ela não estava falando de você! Ela estava falando de... uh... outra pessoa.

# (Após um breve silêncio, Shrek sai do banheiro externo)

# Shrek: Ela não estava falando de mim? Então, de quem ela estava falando?

# (Burro vira as costas para Shrek)

# Burro: Uh-uh, de jeito nenhum. Eu não vou dizer nada. Você não quer me ouvir. Certo? Certo?

# Shrek: Burro!

# Burro: Não!

# Shrek: Certo, olhe. Desculpe, tudo bem?

# (Burro vira a cabeça para trás para levantar a sobrancelha e então desvia o olhar novamente. Shrek suspira)

# Shrek: Desculpa. Acho que sou só um ogro grande, estúpido... feio. Você me perdoa?

# Burro: Ei, é para isso que servem os amigos, certo?

# Shrek: Certo. Amigos?

# Burro: Amigos.

# (Shrek e Burro tremem em cima dele)

# Shrek: Então, o que Fiona disse sobre mim?

# Burro: O que você está me pedindo? Por que você não vai lá perguntar para ela?

# Shrek: O casamento ! Nunca chegaremos a tempo.

# Burro: Ha-ha-ha! Não tema, pois onde há vontade, há um jeito, e eu tenho um jeito.

# (O burro assobia alto, e Shrek olha para cima e vê o dragão voando acima)

# Shrek: Burro?!

# Burro: Acho que é só meu magnetismo animal.

# Shrek: (risos) Ah, venha cá.

# (Shrek dá uma casquinha no Burro)

# Burro: Tudo bem, tudo bem. Não fique babando. Ninguém gosta de puxa-saco. Tudo bem, suba e segure firme. Ainda não tive a chance de colocar os cintos de segurança.

# (Shrek sobe na corrente que ainda está pendurada no pescoço do Dragão. O Dragão levanta o Burro com a mão. Eles decolam, voando através das nuvens até Duloc)

# CATEDRAL DE DULOC - INTERIOR
# (A igreja está lotada de cidadãos. Fiona e Farquaad estão de pé no altar enquanto o padre conduz a cerimônia. Thelonius está por perto, dourando um travesseiro sobre o qual repousam as duas alianças de casamento. Homens com cartões de ponto seguram cartões que dizem "Reverenciado Silêncio")

# Bispo : Povo de Duloc, nos reunimos aqui hoje para testemunhar a união...

# (Fiona olha nervosamente para a janela, percebendo o sol se pondo lentamente em direção ao horizonte)

# Fiona: Hum-

# Bispo: ...do nosso novo rei...

# Fiona: Com licença. Podemos pular para os "sim"?

# (Lord Farquaad ri e então faz um gesto para o bispo dar ouvidos a Fiona)

# Lorde Farquaad: Continue.

# CATEDRAL DE DULOC - EXTERIOR

# (Um grande grupo de guardas está do lado de fora da catedral, de vigia. De repente, o Dragão pousa perto e os guardas fogem aterrorizados. O Dragão olha para trás, para Burro, enquanto Shrek desce das costas dela)

# Burro: Vai lá, divirta-se. Se precisarmos de você, eu assobio. Que tal?

# (O dragão sorri, acena com a cabeça e sai em direção às ruas da cidade. Shrek corre para as portas da catedral, mas o Burro se apressa para ficar em seu caminho)

# Burro: Shrek, espera, espera! Espera um minuto! Você quer fazer isso direito, não é?

# Shrek: Do que você está falando?

# Burro: Tem uma fila, tem uma fila que você tem que esperar. O padre vai dizer: "Fale agora ou cale-se para sempre". E é aí que você diz: "Eu me oponho!"

# Shrek: Ah, não tenho tempo para isso!

# Burro: Ei, espera aí. O que você está fazendo? Escuta aqui!

# (Shrek o empurra, mas Burro o joga contra a porta)

# Burro: Olha, você ama essa mulher, não é?

# Shrek: Sim.

# Burro: Você quer segurá-la?

# Shrek: Sim.

# Burro: Agradá-la?

# Shrek: Sim!

# Burro: (cantando) "Então você tem que, tem que tentar um pouco de ternura". (falando) As garotas adoram essa porcaria romântica!

# Shrek: Tudo bem! Pare com isso! Quando esse cara fala a fala?

# Burro: Temos que dar uma olhada.

# INTERIOR
# (Enquanto o bispo fala, vemos o Burro através de uma das janelas enquanto Shrek o joga para cima para que ele possa ver).

# Bispo: E assim, pelo poder que me foi investido...

# EXTERIOR
# Shrek: O que você vê?!

# Burro: A cidade inteira está lá dentro.

# Bispo: Eu os declaro marido e mulher...

# Burro: Eles estão no altar!

# Bispo: ...rei e rainha.

# Burro: Mãe Fletcher! Ele já disse.

# Shrek: Ah, pelo amor de Deus!

# (Shrek corre para dentro sem pegar o Burro, que cai com força no chão)

# INTERIOR
# (Fiona e Lorde Farquaad estão se inclinando para se beijar, mas são interrompidos quando Shrek irrompe pela porta. Ambos se viram e o veem correndo pelo corredor)

# Shrek: Eu me oponho!

# Fiona: Shrek?

# (Fiona inicialmente parece feliz e surpresa ao vê-lo, mas rapidamente fica chateada. O bispo suspira, fecha o livro e sai silenciosamente)

# Lorde Farquaad: Ah, o que ele quer agora?

# (Toda a congregação fica boquiaberta ao ver Shrek caminhando em direção ao altar. Eles respondem positivamente a ele e começam a fazer "o aceno")

# Shrek: Olá a todos. Estão se divertindo? Eu adoro Duloc, antes de tudo. Muito limpo.

# Fiona: O que você está fazendo aqui?

# Lorde Farquaad: Sério, já é rude o suficiente estar vivo quando ninguém te quer, mas aparecer sem ser convidado em um casamento...

# (Shrek inicialmente parece surpreso com o comentário desnecessariamente duro de Farquaad, mas rapidamente o ignora e volta sua atenção para Fiona)

# Shrek: Fiona! Preciso falar com você.

# Fiona: Ah, agora você quer conversar? Bem, está um pouco tarde para isso, então, se me der licença...

# (Ela se inclina para beijar Farquaad, mas Shrek a puxa pela mão)

# Shrek: Mas você não pode se casar com ele!

# (Ela solta a mão do aperto dele)

# Fiona: E por que não?

# Shrek: Porque ele está se casando com você só para poder ser rei!

# (A multidão fica boquiaberta)

# Lorde Farquaad: Que absurdo! Fiona, não dê ouvidos a ele...

# Shrek: Ele não é seu verdadeiro amor.

# FIONA: E o que você sabe sobre o amor verdadeiro?!

# Shrek: Bem, eu--uh--quero dizer...

# (Fiona fica surpresa com isso)

# Lorde Farquaad: Nossa, que delícia! (risos) O ogro se apaixonou pela princesa! Meu Deus! (risos)

# (Lord Farquaad gesticula para o homem com o cartão de ponto que segura um cartão que diz "Ria". Toda a congregação ri)

# Lorde Farquaad: Um ogro e uma princesa! (risos)

# (Shrek olha para a multidão rindo e depois para o chão, desanimado)

# Fiona: Shrek, isso é verdade?

# Lorde Farquaad: Quem se importa?! É um absurdo! Fiona, meu amor, estamos a apenas um beijo do nosso "felizes para sempre". Agora me beije!

# (Lord Farquaad segura a mão de Fiona, franze os lábios e se inclina em sua direção. Ela olha para ele com desgosto e então desvia sua atenção para a janela. O sol está prestes a se pôr)

# Fiona: "De noite de um jeito, de dia de outro." Eu queria te mostrar antes.

# (Fiona recua e dá a Shrek um sorriso tímido. Quando o sol se põe, ela se transforma em sua versão ogra. A multidão fica boquiaberta e uma pessoa desmaia. Shrek encara Fiona com espanto e então sorri)

# Shrek: Bem, isso explica muita coisa!

# (Fiona olha para Shrek e sorri)

# Lorde Farquaad: Ugh! Que nojo! Guardas! Guardas! Ordeno que os tirem da minha vista agora!

# (Um grande número de guardas corre e agarra Shrek e Fiona)

# Lorde Farquaad: Peguem eles! Peguem os dois!

# Fiona: Não, não! Shrek!

# (Shrek e Fiona tentam agarrar os braços um do outro enquanto são afastados um do outro. Lorde Farquaad agarra sua coroa e a coloca)

# Lorde Farquaad: Toda essa magia não altera nada, este casamento é vinculativo, e isso me torna rei! Vê?! Vê?!

# Fiona: Não, me solta! Shrek!

# Shrek: Não!

# Lorde Farquaad: Não fiquem aí parados, seus idiotas!

# Shrek: Sai da minha frente! Fiona!

# Lorde Farquaad: Mate-o se for preciso, mas pegue-o!

# (Shrek revida com raiva e nocauteia alguns dos guardas, que conseguem subjugá-lo com grande número de homens)

# Lorde Farquaad: Fera, farei você se arrepender do dia em que nos conhecemos! Vou te ver ser esquartejado e esquartejado! Você implorará para que a morte te salve!

# Fiona: Não, Shrek!

# Lorde Farquaad: E quanto a você, minha esposa!

# (Lorde Farquaad puxa uma adaga e a segura na garganta de Fiona)

# Shrek: Fiona!

# Lorde Farquaad: Vou te trancar de volta naquela torre pelo resto dos seus dias! Eu sou o rei!

# (Shrek consegue soltar o braço e assobia alto)

# Lorde Farquaad: Eu quero ordem! Eu quero perfeição! Eu quero...

# (De repente, Dragão, com Burro no topo da cabeça, atravessa uma grande janela atrás dele. Lorde Farquaad larga sua arma e olha para cima.)

# Lorde Farquaad: Aaah! Aah!

# (O dragão desce e o engole de uma só vez. Os guardas fogem ou recuam.)

# Burro: Tudo bem! Ninguém se mexa! Tenho um dragão aqui e não tenho medo de usá-lo.

# (O dragão ruge, fazendo com que a maioria dos guardas se afaste com medo. Os guardas restantes soltam Shrek e Fiona, recuando)

# Burro: Sou um burro no limite!

# (O dragão arrota e a coroa de Lorde Farquaad voa de sua boca e cai no chão)

# Burro: Casamentos de celebridades. Eles nunca duram, não é?

# (A congregação ri e aplaude)

# Burro: Vá em frente, Shrek.

# Shrek: É, Fiona?

# Fiona: Sim, Shrek?

# Shrek: Eu -- eu te amo.

# Fiona: Sério?

# Shrek: Sério, sério.

# Fiona: Eu também te amo.

# (Shrek e Fiona se beijam. Thelonius pega um dos cartões e escreve 'Awwww' no verso e o mostra para a congregação. De repente, a magia do feitiço puxa Fiona para longe. Ela é erguida no ar e paira enquanto a magia age ao seu redor. A voz de Fiona é ouvida, embora ela não esteja movendo os lábios)

# Fiona: "Até você encontrar o primeiro beijo do amor verdadeiro e então assumir a verdadeira forma do amor. Assumir a verdadeira forma do amor. Assumir a verdadeira forma do amor."

# (De repente, os olhos de Fiona se arregalam e se iluminam. A força do feitiço atinge a multidão e todas as janelas. Todas, exceto uma com a imagem de Farquaad, que Dragon quebra com o punho. Fiona é baixada ao chão e Shrek corre até ela)

# Shrek: Fiona? Fiona. Você está bem?

# (Fiona se levanta lentamente, ainda uma ogra)

# Fiona: Bem, sim... Porque eu não entendo. Eu deveria ser bonita.

# Shrek: Mas você é linda.

# (Eles sorriem um para o outro)

# Burro: Eu esperava que esse fosse um final feliz.

# (Shrek e Fiona estão prestes a se beijar quando Shrek coloca a mão sobre a tela para cobrir o beijo).

# O PÂNTANO
# (Shrek e Fiona agora estão unidos em matrimônio no pântano de Shrek. Entre os presentes estão as criaturas de contos de fadas que foram banidas para o pântano, assim como alguns guardas Duloc. Shrek e Fiona caminham pelo corredor até a carruagem que os aguarda, feita de uma cebola gigante. Fiona joga seu buquê, que Cinderela e Branca de Neve tentam pegar. Elas acabam entrando em uma briga de gatos e Dragão pega o buquê. Burro parece nervoso, mas Shrek e Fiona lhe lançam olhares tranquilizadores. Gingy foi curado um pouco e agora tem uma perna e anda com uma bengala de doce).

# Gingy: Deus abençoe a todos nós.

# (Os convidados festejam e dançam enquanto o Burro assume o comando cantando a música dos Monkees. Shrek e Fiona vão embora em sua carruagem. Corta para um livro de histórias que diz "E eles viveram feios para sempre... FIM").

# Burro : (quando ele termina de cantar e a tela escurece) Ah, que engraçado. Ah. Ah. Não consigo respirar. Não consigo respirar.

# O FIM"""

pa.PAUSE = 1  # Espera um segundo entre os comandos


pa.click(x=522, y=1052)
time.sleep(0.2) 

pa.click(x=141, y=9)
time.sleep(0.2)  

pa.click(x=956, y=998)
time.sleep(0.2) 

for integrador in roteiro:
    pa.write(integrador)  
    pa.press("enter")



