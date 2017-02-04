#Ouvidor
Ouvidor é um robô que fica escutando a rádio Educadora FM 24 horas, e tenta transcrever tudo que é dito, o objetivo é demonstrar como é possivel quebrar o esquema de sorteios do programa hora do leite, onde os apresentadores falam qual é o horario do mugido, e no fim do programa eles te ligam, e você deve informar com precisão os horarios.

#Instalação
git clone https://github.com/mthbernardes/EducadoraOuvidor.git

<h1>PROJETO DESENVOLVIDO EM PYTHON3</h1>

#Mac OS
<pre>
brew install rtmpdump ffmpeg
pip3 install -r dependencies.txt
</pre>

#Debian/Ubuntu
<pre>
sudo apt-get install rtmpdump librtmp-dev ffmpeg
pip3 install -r dependencies.txt
</pre>

#Executando Backend
<pre>
screen -S Backend
cd Backend_Ouvidor
python3 Ouvidor.py
CTRL + A + D
</pre>

#Executando Backend
<pre>
screen -S API
cd API_Ouvidor
hug -f Ouvidor.py
</pre>

#FrontEnd
<pre>
Simplesmente coloque ele em um servidor de aplicações Web
Apache
Nginx
IIS
Ou pode usar o proprio python3
cd Frontend_Ouvidor
sudo python3 -m http.server 80
</pre>

#Exemplo resultado
<pre>
http://ouvidor-g4mbler.c9users.io/index.html
</pre>

<h1><b>FFMPEG necessario para o funcionamento do código.</b></h1>
