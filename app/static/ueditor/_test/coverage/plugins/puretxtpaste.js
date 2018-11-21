/* automatically generated by JSCoverage - do not edit */
try {
    if (typeof top === 'object' && top !== null && typeof top.opener === 'object' && top.opener !== null) {
        // this is a browser window that was opened from another window

        if (!top.opener._$jscoverage) {
            top.opener._$jscoverage = {};
        }
    }
}
catch (e) {
}

try {
    if (typeof top === 'object' && top !== null) {
        // this is a browser window

        try {
            if (typeof top.opener === 'object' && top.opener !== null && top.opener._$jscoverage) {
                top._$jscoverage = top.opener._$jscoverage;
            }
        }
        catch (e) {
        }

        if (!top._$jscoverage) {
            top._$jscoverage = {};
        }
    }
}
catch (e) {
}

try {
    if (typeof top === 'object' && top !== null && top._$jscoverage) {
        _$jscoverage = top._$jscoverage;
    }
}
catch (e) {
}
if (typeof _$jscoverage !== 'object') {
    _$jscoverage = {};
}
if (!_$jscoverage['plugins/puretxtpaste.js']) {
    _$jscoverage['plugins/puretxtpaste.js'] = [];
    _$jscoverage['plugins/puretxtpaste.js'][7] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][8] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][9] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][12] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][13] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][14] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][16] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][17] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][19] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][25] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][26] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][27] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][28] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][30] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][31] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][32] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][34] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][38] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][39] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][41] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][55] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][56] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][57] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][59] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][65] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][89] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][91] = 0;
    _$jscoverage['plugins/puretxtpaste.js'][94] = 0;
}
_$jscoverage['plugins/puretxtpaste.js'].source = ["<span class=\"c\">/**</span>", "<span class=\"c\"> * &#32431;&#25991;&#26412;&#31896;&#36148;&#25554;&#20214;</span>", "<span class=\"c\"> * @file</span>", "<span class=\"c\"> * @since 1.2.6.1</span>", "<span class=\"c\"> */</span>", "", "UE<span class=\"k\">.</span>plugins<span class=\"k\">[</span><span class=\"s\">'pasteplain'</span><span class=\"k\">]</span> <span class=\"k\">=</span> <span class=\"k\">function</span><span class=\"k\">()</span><span class=\"k\">{</span>", "    <span class=\"k\">var</span> me <span class=\"k\">=</span> <span class=\"k\">this</span><span class=\"k\">;</span>", "    me<span class=\"k\">.</span>setOpt<span class=\"k\">(</span><span class=\"k\">{</span>", "        <span class=\"s\">'pasteplain'</span><span class=\"k\">:</span><span class=\"k\">false</span><span class=\"k\">,</span>", "        <span class=\"s\">'filterTxtRules'</span> <span class=\"k\">:</span> <span class=\"k\">function</span><span class=\"k\">()</span><span class=\"k\">{</span>", "            <span class=\"k\">function</span> transP<span class=\"k\">(</span>node<span class=\"k\">)</span><span class=\"k\">{</span>", "                node<span class=\"k\">.</span>tagName <span class=\"k\">=</span> <span class=\"s\">'p'</span><span class=\"k\">;</span>", "                node<span class=\"k\">.</span>setStyle<span class=\"k\">();</span>", "            <span class=\"k\">}</span>", "            <span class=\"k\">function</span> removeNode<span class=\"k\">(</span>node<span class=\"k\">)</span><span class=\"k\">{</span>", "                node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>removeChild<span class=\"k\">(</span>node<span class=\"k\">,</span><span class=\"k\">true</span><span class=\"k\">)</span>", "            <span class=\"k\">}</span>", "            <span class=\"k\">return</span> <span class=\"k\">{</span>", "                <span class=\"c\">//&#30452;&#25509;&#21024;&#38500;&#21450;&#20854;&#23383;&#33410;&#28857;&#20869;&#23481;</span>", "                <span class=\"s\">'-'</span> <span class=\"k\">:</span> <span class=\"s\">'script style object iframe embed input select'</span><span class=\"k\">,</span>", "                <span class=\"s\">'p'</span><span class=\"k\">:</span> <span class=\"k\">{</span>$<span class=\"k\">:</span><span class=\"k\">{}}</span><span class=\"k\">,</span>", "                <span class=\"s\">'br'</span><span class=\"k\">:</span><span class=\"k\">{</span>$<span class=\"k\">:</span><span class=\"k\">{}}</span><span class=\"k\">,</span>", "                div<span class=\"k\">:</span> <span class=\"k\">function</span> <span class=\"k\">(</span>node<span class=\"k\">)</span> <span class=\"k\">{</span>", "                    <span class=\"k\">var</span> tmpNode<span class=\"k\">,</span> p <span class=\"k\">=</span> UE<span class=\"k\">.</span>uNode<span class=\"k\">.</span>createElement<span class=\"k\">(</span><span class=\"s\">'p'</span><span class=\"k\">);</span>", "                    <span class=\"k\">while</span> <span class=\"k\">(</span>tmpNode <span class=\"k\">=</span> node<span class=\"k\">.</span>firstChild<span class=\"k\">())</span> <span class=\"k\">{</span>", "                        <span class=\"k\">if</span> <span class=\"k\">(</span>tmpNode<span class=\"k\">.</span>type <span class=\"k\">==</span> <span class=\"s\">'text'</span> <span class=\"k\">||</span> <span class=\"k\">!</span>UE<span class=\"k\">.</span>dom<span class=\"k\">.</span>dtd<span class=\"k\">.</span>$block<span class=\"k\">[</span>tmpNode<span class=\"k\">.</span>tagName<span class=\"k\">])</span> <span class=\"k\">{</span>", "                            p<span class=\"k\">.</span>appendChild<span class=\"k\">(</span>tmpNode<span class=\"k\">);</span>", "                        <span class=\"k\">}</span> <span class=\"k\">else</span> <span class=\"k\">{</span>", "                            <span class=\"k\">if</span> <span class=\"k\">(</span>p<span class=\"k\">.</span>firstChild<span class=\"k\">())</span> <span class=\"k\">{</span>", "                                node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>insertBefore<span class=\"k\">(</span>p<span class=\"k\">,</span> node<span class=\"k\">);</span>", "                                p <span class=\"k\">=</span> UE<span class=\"k\">.</span>uNode<span class=\"k\">.</span>createElement<span class=\"k\">(</span><span class=\"s\">'p'</span><span class=\"k\">);</span>", "                            <span class=\"k\">}</span> <span class=\"k\">else</span> <span class=\"k\">{</span>", "                                node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>insertBefore<span class=\"k\">(</span>tmpNode<span class=\"k\">,</span> node<span class=\"k\">);</span>", "                            <span class=\"k\">}</span>", "                        <span class=\"k\">}</span>", "                    <span class=\"k\">}</span>", "                    <span class=\"k\">if</span> <span class=\"k\">(</span>p<span class=\"k\">.</span>firstChild<span class=\"k\">())</span> <span class=\"k\">{</span>", "                        node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>insertBefore<span class=\"k\">(</span>p<span class=\"k\">,</span> node<span class=\"k\">);</span>", "                    <span class=\"k\">}</span>", "                    node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>removeChild<span class=\"k\">(</span>node<span class=\"k\">);</span>", "                <span class=\"k\">}</span><span class=\"k\">,</span>", "                ol<span class=\"k\">:</span> removeNode<span class=\"k\">,</span>", "                ul<span class=\"k\">:</span> removeNode<span class=\"k\">,</span>", "                dl<span class=\"k\">:</span>removeNode<span class=\"k\">,</span>", "                dt<span class=\"k\">:</span>removeNode<span class=\"k\">,</span>", "                dd<span class=\"k\">:</span>removeNode<span class=\"k\">,</span>", "                <span class=\"s\">'li'</span><span class=\"k\">:</span>removeNode<span class=\"k\">,</span>", "                <span class=\"s\">'caption'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span>", "                <span class=\"s\">'th'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span>", "                <span class=\"s\">'tr'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span>", "                <span class=\"s\">'h1'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span><span class=\"s\">'h2'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span><span class=\"s\">'h3'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span><span class=\"s\">'h4'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span><span class=\"s\">'h5'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span><span class=\"s\">'h6'</span><span class=\"k\">:</span>transP<span class=\"k\">,</span>", "                <span class=\"s\">'td'</span><span class=\"k\">:</span><span class=\"k\">function</span><span class=\"k\">(</span>node<span class=\"k\">)</span><span class=\"k\">{</span>", "                        <span class=\"c\">//&#27809;&#26377;&#20869;&#23481;&#30340;td&#30452;&#25509;&#21024;&#25481;</span>", "                        <span class=\"k\">var</span> txt <span class=\"k\">=</span> <span class=\"k\">!!</span>node<span class=\"k\">.</span>innerText<span class=\"k\">();</span>", "                        <span class=\"k\">if</span><span class=\"k\">(</span>txt<span class=\"k\">)</span><span class=\"k\">{</span>", "                         node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>insertAfter<span class=\"k\">(</span>UE<span class=\"k\">.</span>uNode<span class=\"k\">.</span>createText<span class=\"k\">(</span><span class=\"s\">' &amp;nbsp; &amp;nbsp;'</span><span class=\"k\">),</span>node<span class=\"k\">);</span>", "                    <span class=\"k\">}</span>", "                    node<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>removeChild<span class=\"k\">(</span>node<span class=\"k\">,</span>node<span class=\"k\">.</span>innerText<span class=\"k\">())</span>", "                <span class=\"k\">}</span>", "            <span class=\"k\">}</span>", "        <span class=\"k\">}</span><span class=\"k\">()</span>", "    <span class=\"k\">}</span><span class=\"k\">);</span>", "    <span class=\"c\">//&#26242;&#26102;&#36825;&#37324;&#25903;&#25345;&#19968;&#19979;&#32769;&#29256;&#26412;&#30340;&#23646;&#24615;</span>", "    <span class=\"k\">var</span> pasteplain <span class=\"k\">=</span> me<span class=\"k\">.</span>options<span class=\"k\">.</span>pasteplain<span class=\"k\">;</span>", "", "    <span class=\"c\">/**</span>", "<span class=\"c\">     * &#21551;&#29992;&#25110;&#21462;&#28040;&#32431;&#25991;&#26412;&#31896;&#36148;&#27169;&#24335;</span>", "<span class=\"c\">     * @command pasteplain</span>", "<span class=\"c\">     * @method execCommand</span>", "<span class=\"c\">     * @param { String } cmd &#21629;&#20196;&#23383;&#31526;&#20018;</span>", "<span class=\"c\">     * @example</span>", "<span class=\"c\">     * ```javascript</span>", "<span class=\"c\">     * editor.queryCommandState( 'pasteplain' );</span>", "<span class=\"c\">     * ```</span>", "<span class=\"c\">     */</span>", "", "    <span class=\"c\">/**</span>", "<span class=\"c\">     * &#26597;&#35810;&#24403;&#21069;&#26159;&#21542;&#22788;&#20110;&#32431;&#25991;&#26412;&#31896;&#36148;&#27169;&#24335;</span>", "<span class=\"c\">     * @command pasteplain</span>", "<span class=\"c\">     * @method queryCommandState</span>", "<span class=\"c\">     * @param { String } cmd &#21629;&#20196;&#23383;&#31526;&#20018;</span>", "<span class=\"c\">     * @return { int } &#22914;&#26524;&#22788;&#20110;&#32431;&#25991;&#26412;&#27169;&#24335;&#65292;&#36820;&#22238;1&#65292;&#21542;&#21017;&#65292;&#36820;&#22238;0</span>", "<span class=\"c\">     * @example</span>", "<span class=\"c\">     * ```javascript</span>", "<span class=\"c\">     * editor.queryCommandState( 'pasteplain' );</span>", "<span class=\"c\">     * ```</span>", "<span class=\"c\">     */</span>", "    me<span class=\"k\">.</span>commands<span class=\"k\">[</span><span class=\"s\">'pasteplain'</span><span class=\"k\">]</span> <span class=\"k\">=</span> <span class=\"k\">{</span>", "        queryCommandState<span class=\"k\">:</span> <span class=\"k\">function</span> <span class=\"k\">()</span><span class=\"k\">{</span>", "            <span class=\"k\">return</span> pasteplain <span class=\"k\">?</span> <span class=\"s\">1</span> <span class=\"k\">:</span> <span class=\"s\">0</span><span class=\"k\">;</span>", "        <span class=\"k\">}</span><span class=\"k\">,</span>", "        execCommand<span class=\"k\">:</span> <span class=\"k\">function</span> <span class=\"k\">()</span><span class=\"k\">{</span>", "            pasteplain <span class=\"k\">=</span> <span class=\"k\">!</span>pasteplain<span class=\"k\">|</span><span class=\"s\">0</span><span class=\"k\">;</span>", "        <span class=\"k\">}</span><span class=\"k\">,</span>", "        notNeedUndo <span class=\"k\">:</span> <span class=\"s\">1</span>", "    <span class=\"k\">}</span><span class=\"k\">;</span>", "<span class=\"k\">}</span><span class=\"k\">;</span>"];
_$jscoverage['plugins/puretxtpaste.js'][7]++;
UE.plugins.pasteplain = (function () {
    _$jscoverage['plugins/puretxtpaste.js'][8]++;
    var me = this;
    _$jscoverage['plugins/puretxtpaste.js'][9]++;
    me.setOpt({
        "pasteplain": false, "filterTxtRules": (function () {
            _$jscoverage['plugins/puretxtpaste.js'][12]++;

            function transP(node) {
                _$jscoverage['plugins/puretxtpaste.js'][13]++;
                node.tagName = "p";
                _$jscoverage['plugins/puretxtpaste.js'][14]++;
                node.setStyle();
            }

            _$jscoverage['plugins/puretxtpaste.js'][16]++;

            function removeNode(node) {
                _$jscoverage['plugins/puretxtpaste.js'][17]++;
                node.parentNode.removeChild(node, true);
            }

            _$jscoverage['plugins/puretxtpaste.js'][19]++;
            return ({
                "-": "script style object iframe embed input select",
                "p": {$: {}},
                "br": {$: {}},
                div: (function (node) {
                    _$jscoverage['plugins/puretxtpaste.js'][25]++;
                    var tmpNode, p = UE.uNode.createElement("p");
                    _$jscoverage['plugins/puretxtpaste.js'][26]++;
                    while ((tmpNode = node.firstChild())) {
                        _$jscoverage['plugins/puretxtpaste.js'][27]++;
                        if (((tmpNode.type == "text") || (!UE.dom.dtd.$block[tmpNode.tagName]))) {
                            _$jscoverage['plugins/puretxtpaste.js'][28]++;
                            p.appendChild(tmpNode);
                        }
                        else {
                            _$jscoverage['plugins/puretxtpaste.js'][30]++;
                            if (p.firstChild()) {
                                _$jscoverage['plugins/puretxtpaste.js'][31]++;
                                node.parentNode.insertBefore(p, node);
                                _$jscoverage['plugins/puretxtpaste.js'][32]++;
                                p = UE.uNode.createElement("p");
                            }
                            else {
                                _$jscoverage['plugins/puretxtpaste.js'][34]++;
                                node.parentNode.insertBefore(tmpNode, node);
                            }
                        }
                    }
                    _$jscoverage['plugins/puretxtpaste.js'][38]++;
                    if (p.firstChild()) {
                        _$jscoverage['plugins/puretxtpaste.js'][39]++;
                        node.parentNode.insertBefore(p, node);
                    }
                    _$jscoverage['plugins/puretxtpaste.js'][41]++;
                    node.parentNode.removeChild(node);
                }),
                ol: removeNode,
                ul: removeNode,
                dl: removeNode,
                dt: removeNode,
                dd: removeNode,
                "li": removeNode,
                "caption": transP,
                "th": transP,
                "tr": transP,
                "h1": transP,
                "h2": transP,
                "h3": transP,
                "h4": transP,
                "h5": transP,
                "h6": transP,
                "td": (function (node) {
                    _$jscoverage['plugins/puretxtpaste.js'][55]++;
                    var txt = (!(!node.innerText()));
                    _$jscoverage['plugins/puretxtpaste.js'][56]++;
                    if (txt) {
                        _$jscoverage['plugins/puretxtpaste.js'][57]++;
                        node.parentNode.insertAfter(UE.uNode.createText(" &nbsp; &nbsp;"), node);
                    }
                    _$jscoverage['plugins/puretxtpaste.js'][59]++;
                    node.parentNode.removeChild(node, node.innerText());
                })
            });
        })()
    });
    _$jscoverage['plugins/puretxtpaste.js'][65]++;
    var pasteplain = me.options.pasteplain;
    _$jscoverage['plugins/puretxtpaste.js'][89]++;
    me.commands.pasteplain = {
        queryCommandState: (function () {
            _$jscoverage['plugins/puretxtpaste.js'][91]++;
            return (pasteplain ? 1 : 0);
        }), execCommand: (function () {
            _$jscoverage['plugins/puretxtpaste.js'][94]++;
            pasteplain = ((!pasteplain) | 0);
        }), notNeedUndo: 1
    };
});
