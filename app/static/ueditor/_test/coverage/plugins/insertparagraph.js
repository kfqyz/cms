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
if (!_$jscoverage['plugins/insertparagraph.js']) {
    _$jscoverage['plugins/insertparagraph.js'] = [];
    _$jscoverage['plugins/insertparagraph.js'][20] = 0;
    _$jscoverage['plugins/insertparagraph.js'][22] = 0;
    _$jscoverage['plugins/insertparagraph.js'][25] = 0;
    _$jscoverage['plugins/insertparagraph.js'][26] = 0;
    _$jscoverage['plugins/insertparagraph.js'][27] = 0;
    _$jscoverage['plugins/insertparagraph.js'][29] = 0;
    _$jscoverage['plugins/insertparagraph.js'][30] = 0;
    _$jscoverage['plugins/insertparagraph.js'][32] = 0;
    _$jscoverage['plugins/insertparagraph.js'][33] = 0;
    _$jscoverage['plugins/insertparagraph.js'][34] = 0;
    _$jscoverage['plugins/insertparagraph.js'][35] = 0;
    _$jscoverage['plugins/insertparagraph.js'][37] = 0;
    _$jscoverage['plugins/insertparagraph.js'][39] = 0;
    _$jscoverage['plugins/insertparagraph.js'][40] = 0;
}
_$jscoverage['plugins/insertparagraph.js'].source = ["<span class=\"c\">/**</span>", "<span class=\"c\"> * &#25554;&#20837;&#26032;&#30340;&#27573;&#33853;</span>", "<span class=\"c\"> * @file</span>", "<span class=\"c\"> * @since 1.2.6.1</span>", "<span class=\"c\"> */</span>", "", "", "<span class=\"c\">/**</span>", "<span class=\"c\"> * &#22312;&#24403;&#21069;&#20809;&#26631;&#20301;&#32622;&#22788;&#25554;&#20837;&#26032;&#27573;&#33853;, &#22914;&#26524;&#20809;&#26631;&#24050;&#32463;&#22312;&#27573;&#33853;&#20043;&#20013;&#65292; &#21017;&#20250;&#22312;&#35813;&#27573;&#33853;&#20043;&#21518;&#25554;&#20837;&#19968;&#20010;&#26032;&#30340;&#27573;&#33853;&#12290;</span>", "<span class=\"c\"> * @command insertparagraph</span>", "<span class=\"c\"> * @method execCommand</span>", "<span class=\"c\"> * @param { String } cmd &#21629;&#20196;&#23383;&#31526;&#20018;</span>", "<span class=\"c\"> * @example</span>", "<span class=\"c\"> * ```javascript</span>", "<span class=\"c\"> * //editor&#26159;&#32534;&#36753;&#22120;&#23454;&#20363;</span>", "<span class=\"c\"> * editor.execCommand( 'insertparagraph' );</span>", "<span class=\"c\"> * ```</span>", "<span class=\"c\"> */</span>", "", "UE<span class=\"k\">.</span>commands<span class=\"k\">[</span><span class=\"s\">'insertparagraph'</span><span class=\"k\">]</span> <span class=\"k\">=</span> <span class=\"k\">{</span>", "    execCommand <span class=\"k\">:</span> <span class=\"k\">function</span><span class=\"k\">(</span> cmdName<span class=\"k\">,</span>front<span class=\"k\">)</span> <span class=\"k\">{</span>", "        <span class=\"k\">var</span> me <span class=\"k\">=</span> <span class=\"k\">this</span><span class=\"k\">,</span>", "            range <span class=\"k\">=</span> me<span class=\"k\">.</span>selection<span class=\"k\">.</span>getRange<span class=\"k\">(),</span>", "            start <span class=\"k\">=</span> range<span class=\"k\">.</span>startContainer<span class=\"k\">,</span>tmpNode<span class=\"k\">;</span>", "        <span class=\"k\">while</span><span class=\"k\">(</span>start <span class=\"k\">)</span><span class=\"k\">{</span>", "            <span class=\"k\">if</span><span class=\"k\">(</span>domUtils<span class=\"k\">.</span>isBody<span class=\"k\">(</span>start<span class=\"k\">))</span><span class=\"k\">{</span>", "                <span class=\"k\">break</span><span class=\"k\">;</span>", "            <span class=\"k\">}</span>", "            tmpNode <span class=\"k\">=</span> start<span class=\"k\">;</span>", "            start <span class=\"k\">=</span> start<span class=\"k\">.</span>parentNode<span class=\"k\">;</span>", "        <span class=\"k\">}</span>", "        <span class=\"k\">if</span><span class=\"k\">(</span>tmpNode<span class=\"k\">)</span><span class=\"k\">{</span>", "            <span class=\"k\">var</span> p <span class=\"k\">=</span> me<span class=\"k\">.</span>document<span class=\"k\">.</span>createElement<span class=\"k\">(</span><span class=\"s\">'p'</span><span class=\"k\">);</span>", "            <span class=\"k\">if</span><span class=\"k\">(</span>front<span class=\"k\">)</span><span class=\"k\">{</span>", "                tmpNode<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>insertBefore<span class=\"k\">(</span>p<span class=\"k\">,</span>tmpNode<span class=\"k\">)</span>", "            <span class=\"k\">}</span><span class=\"k\">else</span><span class=\"k\">{</span>", "                tmpNode<span class=\"k\">.</span>parentNode<span class=\"k\">.</span>insertBefore<span class=\"k\">(</span>p<span class=\"k\">,</span>tmpNode<span class=\"k\">.</span>nextSibling<span class=\"k\">)</span>", "            <span class=\"k\">}</span>", "            domUtils<span class=\"k\">.</span>fillNode<span class=\"k\">(</span>me<span class=\"k\">.</span>document<span class=\"k\">,</span>p<span class=\"k\">);</span>", "            range<span class=\"k\">.</span>setStart<span class=\"k\">(</span>p<span class=\"k\">,</span><span class=\"s\">0</span><span class=\"k\">).</span>setCursor<span class=\"k\">(</span><span class=\"k\">false</span><span class=\"k\">,</span><span class=\"k\">true</span><span class=\"k\">);</span>", "        <span class=\"k\">}</span>", "    <span class=\"k\">}</span>", "<span class=\"k\">}</span><span class=\"k\">;</span>", ""];
_$jscoverage['plugins/insertparagraph.js'][20]++;
UE.commands.insertparagraph = {
    execCommand: (function (cmdName, front) {
        _$jscoverage['plugins/insertparagraph.js'][22]++;
        var me = this, range = me.selection.getRange(), start = range.startContainer, tmpNode;
        _$jscoverage['plugins/insertparagraph.js'][25]++;
        while (start) {
            _$jscoverage['plugins/insertparagraph.js'][26]++;
            if (domUtils.isBody(start)) {
                _$jscoverage['plugins/insertparagraph.js'][27]++;
                break;
            }
            _$jscoverage['plugins/insertparagraph.js'][29]++;
            tmpNode = start;
            _$jscoverage['plugins/insertparagraph.js'][30]++;
            start = start.parentNode;
        }
        _$jscoverage['plugins/insertparagraph.js'][32]++;
        if (tmpNode) {
            _$jscoverage['plugins/insertparagraph.js'][33]++;
            var p = me.document.createElement("p");
            _$jscoverage['plugins/insertparagraph.js'][34]++;
            if (front) {
                _$jscoverage['plugins/insertparagraph.js'][35]++;
                tmpNode.parentNode.insertBefore(p, tmpNode);
            }
            else {
                _$jscoverage['plugins/insertparagraph.js'][37]++;
                tmpNode.parentNode.insertBefore(p, tmpNode.nextSibling);
            }
            _$jscoverage['plugins/insertparagraph.js'][39]++;
            domUtils.fillNode(me.document, p);
            _$jscoverage['plugins/insertparagraph.js'][40]++;
            range.setStart(p, 0).setCursor(false, true);
        }
    })
};
