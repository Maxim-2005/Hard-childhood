os.setlocale('rus_rus.1251')
lib = require('Lib')
text = [[
8&_APRWS4pSCXx_49/<S6S4pSR8}XS8_RALX1_:98x<1�C/1S</x_<SxSCXd/LSxE8/LSE1_E1`w:�8LC4<S8x1CC/`SL<X�S6S�8R8dXS9R871RJX1_>:p4R!XS1}1SP1p/_SJXS71<WC/>4SR4!1`@:C8S9R4�S4p1SJXx_<<wSx8x1�S78`S98x91NX1_:ES8_e1Jp/1S98<ASxS8L8_8[SxE81`@:/Sx_RXp�4_S8J/7/S8_SP1N1C8`SJXPXE<@:/SP4�/_S<X`Sx8PX&S4xC4EN/1S�4PRXE<>:_191RWS78AS98RX�SASC1S<[P<[SE1xC<w:x&4!CXS7C1S8__191<WwSE8CW@SdRAJWS6SE1xC8`SASP8<1Cw:&R8EWSPR8�/_wS!4Ex_EX@S47S_8x&8[Sx_1xC1C<>:x4R8E8[SJ/78`SASP8<11S�8E8<1C@:<[P<[S11SxC1dXwSES9R/x4_x_E//S<4C<:&X&S<1d&/`SP1dSxXC1`SxS98�R4d8`SP<x_RS/SE8<1C@:&8d�XS98�Sx8P8<17@Sx8dR1_XS/SxE1pX@:8CXSEX7SR4&4Sp71_@S9<<XAS/S�R8pX5:&X&SE1x1<8@S8P4ESp1<1J87S8x_R<7SC8d/@:x&8<WJ/_WS98SJ1R&X<4Sx_8A!/L@SR8EC<LSR1&5:XSJ/7C/LS9RXJ�C/&8ESP<1x_A}/1S_R1E8d/V>>:C8SCX�8SJCX_WS/S!1x_WwS98<d8�XSxC1dS�XSxC1d@:E1�WSI_8SCX&8C1>S/Sp/_1<[SP1R<8d/@:71�E1�[@SCX�81x_>SC1<WJASp1S>1<<`SE1&:&X_X_WxASCX7SESxXCALSxSXR7/�X7/S7<X�<7/:/<WS&/xC4_WS4S91!1`SJXSx_1&<X7/S�E8`C<7/>:]]
abc(text)
num(text)
x = space(text)
print(x)
print()

text = text: gsub(x, ' ')
text = text: gsub(':', '\n')
text = text: gsub('@', ',')
text = text: gsub('_', '_')
text = text: gsub('6', '-')
text = text: gsub('1', '�')
text = text: gsub('}', '�') -- che'
text = text: gsub('E', '�')
text = text: gsub('d', '�')
--text = text: gsub('r', 'III')
text = text: gsub('X', '�')
text = text: gsub('/', '�')
text = text: gsub('8', '�')
text = text: gsub('p', '?')
text = text: gsub('R', 'p')
text = text: gsub('C', '�')
text = text: gsub('<', '�')
text = text: gsub('&', '�')
text = text: gsub('�', '�') -- D
text = text: gsub('9', '�')
text = text: gsub('J', '�')
text = text: gsub('>', '�')
text = text: gsub('x', '�')
text = text: gsub('_', '�')
text = text: gsub('A', '�')
text = text: gsub('P', '�')
text = text: gsub('W', '�')
text = text: gsub('4', '�')
text = text: gsub('?', '�')

print(text)

io.read()
-- . x E A / 4 X