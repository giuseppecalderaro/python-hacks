#!/usr/bin/env python

import string

code = """%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&
+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*&@%$+]!*__(#!*){%&@++
!_)^$&&%#+)}!@!)&^}**#!_$([$!$}#*^}$+&#[{*{}{((#$]{[$[$$()_#}!@}^@_&%^*!){*^^_$^
]@}#%[%!^[^_})+@&}{@*!(@$%$^)}[_!}(*}#}#___}!](@_{{(*#%!%%+*)^+#%}$+_]#}%!**#!^_
)@)$%%^{_%!@(&{!}$_$[)*!^&{}*#{!)@})!*{^&[&$#@)*@#@_@^_#*!@_#})+[^&!@*}^){%%{&#@
@{%(&{+(#^{@{)%_$[+}]$]^{^#(*}%)@$@}(#{_&]#%#]{_*({(])$%[!}#@@&_)([*]}$}&${^}@(%
(%[@%!}%*$}(*@)}){+@(%@*$&]*^*}*]&$[}*]%]+*}^!}*$^^_()#$^]++@__){&&+((#%+(&+){)$
%&&#($[[+##*%${)_!+{_[})%++)$#))]]]$]@]@($+{&%&%+!!!@]_]+])^*@$(@#${}}#}{%}#+{(@
#__+{{]${]!{(%${%%^)(_*_@+)$]$#_@$)]](}{}$(}*%+!}#+)$%$}+#@*&^{##}+@(%[*@_}{(^]^
+_*{@+[$!!@%$+{_&(#^(([&[][[&@#+}_]&&]}^*&$&)#_^$@$((%)}+{}$#+{+^}&[#[#_+${#[#]{
(@@[%}[}$%+*#$+[%(**!$+@$@&+$_$#!_&&&&{***+)}][}#^!%#&$*)$!%}*&#}}##(^_%^]{+]&&]
}^]#^(}@]&$]*_][])$]{_+})^_}]))()^&)(!*![!&}{][(]})[(*^}$&$_@^$)#${%[$_]!^]}}}*+
*^_(+}^)(%(}{&)[}!$$&&+}&[{%}^+#$]@)^&*%{@}]&!%*%$*&][}&{$&*@{@#]$*_[]%%[#]#*%)@
$_^#%$!{#]^$}%^@^+{($!^($%)]+&}+$@[$*)*&)*%!_!!+@&^*{}%#&{}$!(*^*@]@@})[($!)]]})
})(&+##]##%&##$}@{#_])*%(*(@$)}[+(+_)!{{#^{_@)!&)$}@^^^[$#__+$^!*#%%]_!#$]$&+^}%
@])])%}]#$((^+{{@++^])$^*#[$}*]}}{)@+)[_}*@^%#]]#+()+)(]_[!!!)+)$+&@@])!}+*%]$[]
&&[@+$_&#[$!$${}{%[]#+@)*!#)*!{$#*$%}[(&@$&_@($$]]]_[+(#@}&_}+]@$#_+](}^})!@@}@)
}^]^]*}]+&(@@!!](*@#(++*)]!(^$})&_^@+]{#_@*%^[$[%&_%@%_![&&]&_@*#_}[{{])^$[_$_&_
@%%[@#[@_[&+]}[+)!_#_+++%)[@%$(&$[{#@(}$*![#^#{}_)[$^_$${_@&}*![#*#_+%[@{*^$){)#
#%}]{+((*^]+{})&#$!#(*%({_!^*[{%@_&#){![&]@$#[#(!{*#^*%)]!%(#]%${*_^{+}(@}{_^(](
_+!_)^&}!#([(+&[@])[_(]@]@&@{#@(%[@+[^@%@+]*_[{]$[_(_@[!]]^%+@#(@$}]@(^**+]%^)^(
@}^[]@@[@[@}^(^!]%*_]&$!!^^#*[#*[*_}+[$#(_#%@](+[^+}%{_*#]+*(]}!$(%@%#^)}]_&]{${
}$[*{+&+&}[#_#}_(}){^#{[_%*!$+[#)%]@&&_{)#[+*&+#!&)%)%++$_}){%%*@!*&%__(_!]#$*(_
$^!@@}_())%(&$%]]{{{@+!&%@(^!+*{%[*[!]){(#$@)(^{]%[&*(&!{&}!%*$)*]]$%(__[}_+&)!(
^_&*]*+#@{@[_({$*&}][(*!+$+#%&![%^)^#(#}+*+(@)&&!({^^_*($^+)&{)%$@%)&!$$&&^+#[)$
+!$^]*!%^_$}$+!!&%_&){$%{((&^{{(&_&_]{^}@[$^+]}]^{@!^@_%_{^@*)+^*#$#!+*}#)}@(}!]
_*)}$**@}[^_&*^)*+#()]&{{]*+#${@&}#)$[]_+(^_@^][]_)*^*+_!{&$##]((](}}{[!$#_{&{){
*_{^}$#!+]{[^&++*#!]*)]%$!{#^&%(%^*}@^+__])_$@_^#[{{})}$*]#%]{}{][@^!@)_[}{())%)
())&#@*[#}+#^}#%!![#&*}^{^(({+#*[!{!}){(!*@!+@[_(*^+*]$]+@+*_##)&)^(@$^]e@][#&)(
%%{})+^$))[{))}&$(^+{&(#%*@&*(^&{}+!}_!^($}!(}_@@++$)(%}{!{_]%}$!){%^%%@^%&#([+[
_+%){{}(#_}&{&++!@_)(_+}%_#+]&^)+]_[@]+$!+{@}$^!&)#%#^&+$@[+&+{^{*[@]#!{_*[)(#[[
]*!*}}*_(+&%{&#$&+*_]#+#]!&*@}$%)!})@&)*}#(@}!^(]^@}]#&%)![^!$*)&_]^%{{}(!)_&{_{
+[_*+}]$_[#@_^]*^*#@{&%})*{&**}}}!_!+{&^)__)@_#$#%{+)^!{}^@[$+^}&(%%)&!+^_^#}^({
*%]&@{]++}@$$)}#]{)!+@[^)!#[%@^!!+{(@&+++_{!$}{]_%_#^#%&{!_(#$%%&@[})]+_@!(*[_@[
*_&+][^][}^@}])!(&^*[_%+(}!!{!!^*@!({%]#[_&()$]!$]@}*][)#()})[*^[^}]#(((_^#%%]@}
^###%!{(@+]$%*^}(![$@*]_{#*!$*@%*(^+#!)$&]*%$&*@$[)_$!&+_[$)%_*((%+##*]@+#*[$$)^
@)]}!)$^%+%&_#+]&&_!(}+^*#)$%%^+&%^_]@*%^^_#]%{%[&(*_(%(*{^@[@&+!@&[+[++$})$!*}+
(_^%%*}^{+}(+]]_][_(@}^#_{_}*){*)}+*)%#%++}{}__%$$$[%%*})_#*!_!%&*$!]!}{*+{^()$}
*$%*$]][{@+*]_*&!^]_*!_{_@(}+%#$+@}_]#@$#^%((#$%+++]])#*@)&([^#]_$%$)[#)){({%@_^
@#}@*!!()[]%$*+*{*$%@**!}&#[*#[[{(@&_){{!}!)++@*{{({_!#^]}+{{#]{$^)&]%}})^@&$%@$
$!_+!{]*^_+@&@){#*!_#+{[@$^(__}*[^$&{&]!(&+++_@+)&}))$%]${+*!(#@(}&&&!)!_!$&@&{[
[@!#!]]#%)(_^!{*[{^{]})$)^&(*)%}#]#()^#+}!{_}*+{@&_^)+%@!%%${$&%}(%*_!)%$((+$&^^
}#[@%+)&^!](]%+_{{]}@]+^]{(!_*&@][]@_%}%(%&)})&!#)[_]^+$)[(%*%({]$[(#+&+[@[*([$#
^*!@{]]#![[{_]#^@])_[[+%]#[%[+_{)^+([^}[]_[}])*^!_+$}^+_)+*@$$^}(&[)_^[+})^]&)))
}*+}%){@_)]_)&)!@)*#^_%{}(]]$)+^@+}+$_*&)]%^@&)![!@$[@)@}%!)@$((^![{(%([+#&{$+#[
#&)!+{)__]+%)![*%^&*^)*#[&(_%*)^_%*^{&_[@%%@^%_}&*@($[@$$#](}&$*&$$((!!}{%!^^$}!
{]][(!_(+}$%*_]*&$!_[@$})#@)]*%#]*{)$@*!^#[]**+]&])$@*@]{$_+]]^_*+*+)%!_!}#}^@*[
$[##&_^+&)((_$#!]}[_*]_$^_*{[^$#[{@$[()+*@_$((+}*^!]){][_}!)%{}{&#@[&#$(}#}%%{!_
@)[($}&+&$}}%[)@[{^_+%+[)[^[*{{^#]*__$^%^}#]}*{^+{!@#(+*]$)^(*!^^]^)[}@{%(($(+_#
*){@}]+}&)[(^^(*$&_$@#[#_$)^_()}{[]]{^@*)_!{@)(!))^!(]$*@${{]%@*{}&#$#!%++#[})!^}^[+$*!*_$[]%_+&#{^@[}@#&)%})+^&]$@_}[%&(}^!_}{)_{$]_@{%*_&^_+{$[__]^&*}]]#}_{{($)_#%(][+}+)#]#}(_@@^*!)_)[^$
@^&$^@*}_[!+^!#{^}!{[$[{{++^[^[^+#!!&{]@(*+#{({)%[%]&(_[*{_]#%+!*#$]}#[_$!%_}*)(*_+}_&%&{})
&+(]({$]{+%*}]@+_^*}&!!*^_{(]]}_!]]((!+$(^*()#*%[!])*%[)#*!&[@+!#]_$++!$%}*&!)}_&%((@{+]@^}**((!%!$+&#][_#}$)_@!}[*%&}%&}[^$$*([&(_*#+}+^)&)^+&{)^$*}}%@^+@%^)}!!%#+_@{{^%@}#&##*!_&^{%$_{_+%)#{{!$[&&]#^)+!]*&]{[!^)%}}*%
_{{$%_+*^{+!*!$)}*)_&%@[$*!&*#][!!&#{]$}}]^_$*!*&]&(@%_$*@+!{}^^+()+_$(!]*@)&#[#
(#[@!$[+"""

if __name__ == '__main__':
    print("Level 3");
    identity = string.maketrans('', '');
    print(code.translate(identity,string.letters));

