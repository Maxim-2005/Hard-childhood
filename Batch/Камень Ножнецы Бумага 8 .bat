@echo off
chcp 1251
cls
title ������ ������� ������
:1
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/-............---:yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy--............----:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:-..............----:oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+-................----:+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd--.................-----:yNMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo--...................----:+mMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/-.......................---/NMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/-.........................--hMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMNsoNMMMMMMMMMMMMMMMMN:-.......-.............-...-:dMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMNo`.hMMMMMMMMMMMMMMMMd-.....-...............--...-+NMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMNh/-.:NMMMMMMMMMMMMMMMN+-....................::...-/NMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMMMNo-..-dMMMMMMMMMMMMMMMMm-.....-...............::-../mMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMMNh/.../dMMMMMMMMMMMMMMMMMN/....................-///-oNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMMd+-...+NMMMMMMMMMMMMMMMMMMMmo:...........```....--/+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMMy:-...oNMMMMMMMMMMMMMNNNdhhdMMNs--.`......``.......:+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMMy:....-dMMMMMMMMNdhso+/--...`hMMMmyo...-------......-+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMMMy:------:+yhhys+:-..--.....-:+mMMMMMMmo//:--..----.../mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: MMMMMMMMMMMMNs:-----....--.........--/shmNMMMMMMMMMMMMMNds+:--/hmddNMMdssdMMMMMMMMMMMMMMMMMMMMMMMMMM
echo: hhhhdddmmdhs/----..............-/oydNMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMs-``:NMMMMMMMMMMMMMMMMMMMMMMMMM
echo: /--------------...............omdhysoo++++++++oomMMMMMMMMMMMMMMMMMMMMy-...sMMMMMMMMMMMMMMMMMMMMMMMMM
echo: :-.....-......................---...--........``oMMMMMMMMMMMMMMMMMMMMN/.---sMMMMMMMMMMMMMMMMMMMMMMMM
echo: :.......................................-://+++/dMMMMMMMMMMMMMMMMMMMMMd-....sNMMMMMMMMMMMMMMMMMMMMMM
echo: :..............................:oossyhdmNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMo....-oNMMMMMMMMMMMMMMMMMMMMM
echo: :..............................://+osyhddddhdNMMMMMMMMMMMMmhdNMMMMMMMMMN/.----sMMMMMMMMMMMMMMMMMMMMM
echo: :.................................--...----..yMMMMMMMMMMMo.`-/hNMMMMMMMMd-....-hMMMMMMMMMMMMMMMMMMMM
echo: /------......................-:::---------:::hMMMMMMMMMMMo-...-/hNMMMMMMMs-....-yssdmMMMMMMMMMMMMMMM
echo: /:::::--------.............../hmmmmmmmmmmmmNNMMMMMMMMMMMMNh/.....:odNMMMMNo.....--.-:oyyyhhmNMMMMMMM
echo: mmdddddddhyso/:-----------....-/ymMMMMMMMMMMMMMMMMMMMMMMMMMNy/.....-/sdNMMN+...............:+mMMMMMM
echo: MMMMMMMMMMMMMNmdyyssyhddhyo+:-.-.-+hmNMMMMMMMMMMMMMMMMMMMMMMMNy:..--..-/ymmo................-/dMMMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMNmdy+:.---/yNMMMMMMMMMMMMMMMMMMMMMMMmy/-......:-..................-:sNMMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho/-..dMMMMMMMMMMMMMMMMMMMMMMMMMNh/-.........................--+NMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyNMMMMMMMMMMMMMMMMMMMMMMMMMMMNdo-............-...........--sMM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh/............--.........--:NM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:-...--.......-........--:dM
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/---....--.....-.......---oN
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs------...--............---s
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd:-----------...........----
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMds/::::------...........---
echo: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyo/:::----..........--
choice /c 123 /n /m "�������� 1-������ 2-������� ��� 3-������: "
set knb=%errorlevel%cls
if %knb%==1 (echo ��: ������)
if %knb%==2 (echo ��: �������)
if %knb%==3 (echo ��: ������)
set /a RND=1+3*%random%/32767
if %rnd%==1 (echo ��: ������)
if %rnd%==2 (echo ��: �������)
if %rnd%==3 (echo ��: ������)
set /a GAME=%GAME%+1
::�����
if %rnd%==%knb% (echo ����� & set /a DRAW=%DRAW%+1)
::������
if %knb%==1 (if %rnd%==2 (echo �� �������� & set /a WIN=%WIN%+1))
if %knb%==2 (if %rnd%==3 (echo �� �������� & set /a WIN=%WIN%+1))
if %knb%==3 (if %rnd%==1 (echo �� �������� & set /a WIN=%WIN%+1))
::��������
if %knb%==1 (if %rnd%==3 (echo �� ��������� & set /a LOSE=%LOSE%+1))
if %knb%==2 (if %rnd%==1 (echo �� ��������� & set /a LOSE=%LOSE%+1))
if %knb%==3 (if %rnd%==2 (echo �� ��������� & set /a LOSE=%LOSE%+1))

echo ����� ���: %GAME% ������: %DRAW% �����: %WIN% ���������: %LOSE%
goto 1



