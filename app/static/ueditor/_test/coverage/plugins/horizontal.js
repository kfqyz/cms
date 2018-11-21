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
if (!_$jscoverage['plugins/horizontal.js']) {
    _$jscoverage['plugins/horizontal.js'] = [];
    _$jscoverage['plugins/horizontal.js'][28] = 0;
    _$jscoverage['plugins/horizontal.js'][29] = 0;
    _$jscoverage['plugins/horizontal.js'][30] = 0;
    _$jscoverage['plugins/horizontal.js'][32] = 0;
    _$jscoverage['plugins/horizontal.js'][33] = 0;
    _$jscoverage['plugins/horizontal.js'][34] = 0;
    _$jscoverage['plugins/horizontal.js'][35] = 0;
    _$jscoverage['plugins/horizontal.js'][37] = 0;
    _$jscoverage['plugins/horizontal.js'][39] = 0;
    _$jscoverage['plugins/horizontal.js'][40] = 0;
    _$jscoverage['plugins/horizontal.js'][41] = 0;
    _$jscoverage['plugins/horizontal.js'][42] = 0;
    _$jscoverage['plugins/horizontal.js'][43] = 0;
    _$jscoverage['plugins/horizontal.js'][44] = 0;
    _$jscoverage['plugins/horizontal.js'][45] = 0;
    _$jscoverage['plugins/horizontal.js'][48] = 0;
    _$jscoverage['plugins/horizontal.js'][49] = 0;
    _$jscoverage['plugins/horizontal.js'][50] = 0;
    _$jscoverage['plugins/horizontal.js'][56] = 0;
    _$jscoverage['plugins/horizontal.js'][62] = 0;
    _$jscoverage['plugins/horizontal.js'][98] = 0;
    _$jscoverage['plugins/horizontal.js'][99] = 0;
    _$jscoverage['plugins/horizontal.js'][100] = 0;
    _$jscoverage['plugins/horizontal.js'][101] = 0;
    _$jscoverage['plugins/horizontal.js'][102] = 0;
    _$jscoverage['plugins/horizontal.js'][103] = 0;
    _$jscoverage['plugins/horizontal.js'][104] = 0;
    _$jscoverage['plugins/horizontal.js'][105] = 0;
    _$jscoverage['plugins/horizontal.js'][106] = 0;
    _$jscoverage['plugins/horizontal.js'][107] = 0;
    _$jscoverage['plugins/horizontal.js'][108] = 0;
}
_$jscoverage['plugins/horizontal.js'].source = ["<span class=\"c\">/**</span>", "<span class=\"c\"> * &#25554;&#20837;&#20998;&#21106;&#32447;&#25554;&#20214;</span>", "<span class=\"c\"> * @file</span>", "<span class=\"c\"> * @since 1.2.6.1</span>", "<span class=\"c\"> */</span>", "", "<span class=\"c\">/**</span>", "<span class=\"c\"> * &#25554;&#20837;&#20998;&#21106;&#32447;&#65292;&#20998;&#21106;&#32447;&#26159;hr&#26631;&#31614;</span>", "<span class=\"c\"> * @command horizontal</span>", "<span class=\"c\"> * @method execCommand</span>", "<span class=\"c\"> * @param { String } cmdName &#21629;&#20196;&#23383;&#31526;&#20018;</span>", "<span class=\"c\"> * @example</span>", "<span class=\"c\"> * ```javascript</span>", "<span class=\"c\"> * editor.execCommand( 'horizontal' );</span>", "<span class=\"c\"> * ```</span>", "<span class=\"c\"> */</span>", "", "<span class=\"c\">/**</span>", "<span class=\"c\"> * &#26597;&#35810;&#24403;&#21069;&#26159;&#21542;&#20801;&#35768;&#25554;&#20837;&#20998;&#21106;&#32447;</span>", "<span class=\"c\"> * @command horizontal</span>", "<span class=\"c\"> * @method queryCommandState</span>", "<span class=\"c\"> * @return { Int } &#22914;&#26524;&#36873;&#21306;&#22312;&#34920;&#26684;&#37324;&#38754;&#65292;&#36820;&#22238;0&#65292;&#21542;&#21017;&#36820;&#22238;1</span>", "<span class=\"c\"> * @example</span>", "<span class=\"c\"> * ```javascript</span>", "<span class=\"c\"> * editor.queryCommandState( 'horizontal' );</span>", "<span class=\"c\"> * ```</span>", "<span class=\"c\"> */</span>", "UE<span class=\"k\">.</span>plugins<span class=\"k\">[</span><span class=\"s\">'horizontal'</span><span class=\"k\">]</span> <span class=\"k\">=</span> <span class=\"k\">function</span><span class=\"k\">()</span><span class=\"k\">{</span>", "    <span class=\"k\">var</span> me <span class=\"k\">=</span> <span class=\"k\">this</span><span class=\"k\">;</span>", "    me<span class=\"k\">.</span>commands<span class=\"k\">[</span><span class=\"s\">'horizontal'</span><span class=\"k\">]</span> <span class=\"k\">=</span> <span class=\"k\">{</span>", "        execCommand <span class=\"k\">:</span> <span class=\"k\">function</span><span class=\"k\">(</span> cmdName <span class=\"k\">)</span> <span class=\"k\">{</span>", "            <span class=\"k\">var</span> me <span class=\"k\">=</span> <span class=\"k\">this</span><span class=\"k\">;</span>", "            <span class=\"k\">if</span><span class=\"k\">(</span>me<span class=\"k\">.</span>queryCommandState<span class=\"k\">(</span>cmdName<span class=\"k\">)!==-</span><span class=\"s\">1</span><span class=\"k\">)</span><span class=\"k\">{</span>", "                me<span class=\"k\">.</span>execCommand<span class=\"k\">(</span><span class=\"s\">'insertHtml'</span><span class=\"k\">,</span><span class=\"s\">'&lt;hr&gt;'</span><span class=\"k\">);</span>", "                <span class=\"k\">var</span> range <span class=\"k\">=</span> me<span class=\"k\">.</span>selection<span class=\"k\">.</span>getRange<span class=\"k\">(),</span>", "                    start <span class=\"k\">=</span> range<span class=\"k\">.</span>startContainer<span class=\"k\">;</span>", "                <span class=\"k\">if</span><span class=\"k\">(</span>start<span class=\"k\">.</span>nodeType <span class=\"k\">==</span> <span class=\"s\">1</span> <span class=\"k\">&amp;&amp;</span> <span class=\"k\">!</span>start<span class=\"k\">.</span>childNodes<span class=\"k\">[</span>range<span class=\"k\">.</span>startOffset<span class=\"k\">]</span> <span class=\"k\">)</span><span class=\"k\">{</span>", "", "                    <span class=\"k\">var</span> tmp<span class=\"k\">;</span>", "                    <span class=\"k\">if</span><span class=\"k\">(</span>tmp <span class=\"k\">=</span> start<span class=\"k\">.</span>childNodes<span class=\"k\">[</span>range<span class=\"k\">.</span>startOffset <span class=\"k\">-</span> <span class=\"s\">1</span><span class=\"k\">])</span><span class=\"k\">{</span>", "                        <span class=\"k\">if</span><span class=\"k\">(</span>tmp<span class=\"k\">.</span>nodeType <span class=\"k\">==</span> <span class=\"s\">1</span> <span class=\"k\">&amp;&amp;</span> tmp<span class=\"k\">.</span>tagName <span class=\"k\">==</span> <span class=\"s\">'HR'</span><span class=\"k\">)</span><span class=\"k\">{</span>", "                            <span class=\"k\">if</span><span class=\"k\">(</span>me<span class=\"k\">.</span>options<span class=\"k\">.</span>enterTag <span class=\"k\">==</span> <span class=\"s\">'p'</span><span class=\"k\">)</span><span class=\"k\">{</span>", "                                tmp <span class=\"k\">=</span> me<span class=\"k\">.</span>document<span class=\"k\">.</span>createElement<span class=\"k\">(</span><span class=\"s\">'p'</span><span class=\"k\">);</span>", "                                range<span class=\"k\">.</span>insertNode<span class=\"k\">(</span>tmp<span class=\"k\">);</span>", "                                range<span class=\"k\">.</span>setStart<span class=\"k\">(</span>tmp<span class=\"k\">,</span><span class=\"s\">0</span><span class=\"k\">).</span>setCursor<span class=\"k\">();</span>", "", "                            <span class=\"k\">}</span><span class=\"k\">else</span><span class=\"k\">{</span>", "                                tmp <span class=\"k\">=</span> me<span class=\"k\">.</span>document<span class=\"k\">.</span>createElement<span class=\"k\">(</span><span class=\"s\">'br'</span><span class=\"k\">);</span>", "                                range<span class=\"k\">.</span>insertNode<span class=\"k\">(</span>tmp<span class=\"k\">);</span>", "                                range<span class=\"k\">.</span>setStartBefore<span class=\"k\">(</span>tmp<span class=\"k\">).</span>setCursor<span class=\"k\">();</span>", "                            <span class=\"k\">}</span>", "                        <span class=\"k\">}</span>", "                    <span class=\"k\">}</span>", "", "                <span class=\"k\">}</span>", "                <span class=\"k\">return</span> <span class=\"k\">true</span><span class=\"k\">;</span>", "            <span class=\"k\">}</span>", "", "        <span class=\"k\">}</span><span class=\"k\">,</span>", "        <span class=\"c\">//&#36793;&#30028;&#22312;table&#37324;&#19981;&#33021;&#21152;&#20998;&#38548;&#32447;</span>", "        queryCommandState <span class=\"k\">:</span> <span class=\"k\">function</span><span class=\"k\">()</span> <span class=\"k\">{</span>", "            <span class=\"k\">return</span> domUtils<span class=\"k\">.</span>filterNodeList<span class=\"k\">(</span><span class=\"k\">this</span><span class=\"k\">.</span>selection<span class=\"k\">.</span>getStartElementPath<span class=\"k\">(),</span><span class=\"s\">'table'</span><span class=\"k\">)</span> <span class=\"k\">?</span> <span class=\"k\">-</span><span class=\"s\">1</span> <span class=\"k\">:</span> <span class=\"s\">0</span><span class=\"k\">;</span>", "        <span class=\"k\">}</span>", "    <span class=\"k\">}</span><span class=\"k\">;</span>", "<span class=\"c\">//    me.addListener('delkeyup',function(){</span>", "<span class=\"c\">//        var rng = this.selection.getRange();</span>", "<span class=\"c\">//        if(browser.ie &amp;&amp; browser.version &gt; 8){</span>", "<span class=\"c\">//            rng.txtToElmBoundary(true);</span>", "<span class=\"c\">//            if(domUtils.isStartInblock(rng)){</span>", "<span class=\"c\">//                var tmpNode = rng.startContainer;</span>", "<span class=\"c\">//                var pre = tmpNode.previousSibling;</span>", "<span class=\"c\">//                if(pre &amp;&amp; domUtils.isTagNode(pre,'hr')){</span>", "<span class=\"c\">//                    domUtils.remove(pre);</span>", "<span class=\"c\">//                    rng.select();</span>", "<span class=\"c\">//                    return;</span>", "<span class=\"c\">//                }</span>", "<span class=\"c\">//            }</span>", "<span class=\"c\">//        }</span>", "<span class=\"c\">//        if(domUtils.isBody(rng.startContainer)){</span>", "<span class=\"c\">//            var hr = rng.startContainer.childNodes[rng.startOffset -1];</span>", "<span class=\"c\">//            if(hr &amp;&amp; hr.nodeName == 'HR'){</span>", "<span class=\"c\">//                var next = hr.nextSibling;</span>", "<span class=\"c\">//                if(next){</span>", "<span class=\"c\">//                    rng.setStart(next,0)</span>", "<span class=\"c\">//                }else if(hr.previousSibling){</span>", "<span class=\"c\">//                    rng.setStartAtLast(hr.previousSibling)</span>", "<span class=\"c\">//                }else{</span>", "<span class=\"c\">//                    var p = this.document.createElement('p');</span>", "<span class=\"c\">//                    hr.parentNode.insertBefore(p,hr);</span>", "<span class=\"c\">//                    domUtils.fillNode(this.document,p);</span>", "<span class=\"c\">//                    rng.setStart(p,0);</span>", "<span class=\"c\">//                }</span>", "<span class=\"c\">//                domUtils.remove(hr);</span>", "<span class=\"c\">//                rng.setCursor(false,true);</span>", "<span class=\"c\">//            }</span>", "<span class=\"c\">//        }</span>", "<span class=\"c\">//    })</span>", "    me<span class=\"k\">.</span>addListener<span class=\"k\">(</span><span class=\"s\">'delkeydown'</span><span class=\"k\">,</span><span class=\"k\">function</span><span class=\"k\">(</span>name<span class=\"k\">,</span>evt<span class=\"k\">)</span><span class=\"k\">{</span>", "        <span class=\"k\">var</span> rng <span class=\"k\">=</span> <span class=\"k\">this</span><span class=\"k\">.</span>selection<span class=\"k\">.</span>getRange<span class=\"k\">();</span>", "        rng<span class=\"k\">.</span>txtToElmBoundary<span class=\"k\">(</span><span class=\"k\">true</span><span class=\"k\">);</span>", "        <span class=\"k\">if</span><span class=\"k\">(</span>domUtils<span class=\"k\">.</span>isStartInblock<span class=\"k\">(</span>rng<span class=\"k\">))</span><span class=\"k\">{</span>", "            <span class=\"k\">var</span> tmpNode <span class=\"k\">=</span> rng<span class=\"k\">.</span>startContainer<span class=\"k\">;</span>", "            <span class=\"k\">var</span> pre <span class=\"k\">=</span> tmpNode<span class=\"k\">.</span>previousSibling<span class=\"k\">;</span>", "            <span class=\"k\">if</span><span class=\"k\">(</span>pre <span class=\"k\">&amp;&amp;</span> domUtils<span class=\"k\">.</span>isTagNode<span class=\"k\">(</span>pre<span class=\"k\">,</span><span class=\"s\">'hr'</span><span class=\"k\">))</span><span class=\"k\">{</span>", "                domUtils<span class=\"k\">.</span>remove<span class=\"k\">(</span>pre<span class=\"k\">);</span>", "                rng<span class=\"k\">.</span>select<span class=\"k\">();</span>", "                domUtils<span class=\"k\">.</span>preventDefault<span class=\"k\">(</span>evt<span class=\"k\">);</span>", "                <span class=\"k\">return</span> <span class=\"k\">true</span><span class=\"k\">;</span>", "", "            <span class=\"k\">}</span>", "        <span class=\"k\">}</span>", "", "    <span class=\"k\">}</span><span class=\"k\">)</span>", "<span class=\"k\">}</span><span class=\"k\">;</span>", ""];
_$jscoverage['plugins/horizontal.js'][28]++;
UE.plugins.horizontal = (function () {
    _$jscoverage['plugins/horizontal.js'][29]++;
    var me = this;
    _$jscoverage['plugins/horizontal.js'][30]++;
    me.commands.horizontal = {
        execCommand: (function (cmdName) {
            _$jscoverage['plugins/horizontal.js'][32]++;
            var me = this;
            _$jscoverage['plugins/horizontal.js'][33]++;
            if ((me.queryCommandState(cmdName) !== -1)) {
                _$jscoverage['plugins/horizontal.js'][34]++;
                me.execCommand("insertHtml", "<hr>");
                _$jscoverage['plugins/horizontal.js'][35]++;
                var range = me.selection.getRange(), start = range.startContainer;
                _$jscoverage['plugins/horizontal.js'][37]++;
                if (((start.nodeType == 1) && (!start.childNodes[range.startOffset]))) {
                    _$jscoverage['plugins/horizontal.js'][39]++;
                    var tmp;
                    _$jscoverage['plugins/horizontal.js'][40]++;
                    if ((tmp = start.childNodes[(range.startOffset - 1)])) {
                        _$jscoverage['plugins/horizontal.js'][41]++;
                        if (((tmp.nodeType == 1) && (tmp.tagName == "HR"))) {
                            _$jscoverage['plugins/horizontal.js'][42]++;
                            if ((me.options.enterTag == "p")) {
                                _$jscoverage['plugins/horizontal.js'][43]++;
                                tmp = me.document.createElement("p");
                                _$jscoverage['plugins/horizontal.js'][44]++;
                                range.insertNode(tmp);
                                _$jscoverage['plugins/horizontal.js'][45]++;
                                range.setStart(tmp, 0).setCursor();
                            }
                            else {
                                _$jscoverage['plugins/horizontal.js'][48]++;
                                tmp = me.document.createElement("br");
                                _$jscoverage['plugins/horizontal.js'][49]++;
                                range.insertNode(tmp);
                                _$jscoverage['plugins/horizontal.js'][50]++;
                                range.setStartBefore(tmp).setCursor();
                            }
                        }
                    }
                }
                _$jscoverage['plugins/horizontal.js'][56]++;
                return true;
            }
        }), queryCommandState: (function () {
            _$jscoverage['plugins/horizontal.js'][62]++;
            return (domUtils.filterNodeList(this.selection.getStartElementPath(), "table") ? -1 : 0);
        })
    };
    _$jscoverage['plugins/horizontal.js'][98]++;
    me.addListener("delkeydown", (function (name, evt) {
        _$jscoverage['plugins/horizontal.js'][99]++;
        var rng = this.selection.getRange();
        _$jscoverage['plugins/horizontal.js'][100]++;
        rng.txtToElmBoundary(true);
        _$jscoverage['plugins/horizontal.js'][101]++;
        if (domUtils.isStartInblock(rng)) {
            _$jscoverage['plugins/horizontal.js'][102]++;
            var tmpNode = rng.startContainer;
            _$jscoverage['plugins/horizontal.js'][103]++;
            var pre = tmpNode.previousSibling;
            _$jscoverage['plugins/horizontal.js'][104]++;
            if ((pre && domUtils.isTagNode(pre, "hr"))) {
                _$jscoverage['plugins/horizontal.js'][105]++;
                domUtils.remove(pre);
                _$jscoverage['plugins/horizontal.js'][106]++;
                rng.select();
                _$jscoverage['plugins/horizontal.js'][107]++;
                domUtils.preventDefault(evt);
                _$jscoverage['plugins/horizontal.js'][108]++;
                return true;
            }
        }
    }));
});
