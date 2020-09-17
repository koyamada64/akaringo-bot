# -*- coding: utf-8 -*-
import unittest
import re
import MeCab
import sqlite3
from collections import defaultdict


class PrepareChain(object):
    BEGIN = u"__BEGIN_SENTENCE__"
    END = u"__END_SENTENCE__"

    DB_PATH = "chain.db"
    DB_SCHEMA_PATH = "schema.sql"

    def __init__(self, text):
        self.text=text

        # 蠖｢諷狗ｴ�隗｣譫千畑繧ｿ繧ｬ繝ｼ
        self.tagger = MeCab.Tagger('-Ochasen')

    def make_triplet_freqs(self):
        # 髟ｷ縺�譁�遶�繧偵そ繝ｳ繝�繝ｳ繧ｹ豈弱↓蛻�蜑ｲ
        sentences = self._divide(self.text)

        # 3縺､邨�縺ｮ蜃ｺ迴ｾ蝗樊焚
        triplet_freqs = defaultdict(int)

        # 繧ｻ繝ｳ繝�繝ｳ繧ｹ豈弱↓3縺､邨�縺ｫ縺吶ｋ
        for sentence in sentences:
            # 蠖｢諷狗ｴ�隗｣譫�
            morphemes = self._morphological_analysis(sentence)
            # 3縺､邨�繧偵▽縺上ｋ
            triplets = self._make_triplet(morphemes)
            # 蜃ｺ迴ｾ蝗樊焚繧貞刈邂�
            for (triplet, n) in triplets.items():
                triplet_freqs[triplet] += n

        return triplet_freqs

    def _divide(self, text):
        # 謾ｹ陦梧枚蟄嶺ｻ･螟悶�ｮ蛻�蜑ｲ譁�蟄暦ｼ域ｭ｣隕剰｡ｨ迴ｾ陦ｨ險假ｼ�
        delimiter = u"。|\?|\!|？|！|．|\."

        # 蜈ｨ縺ｦ縺ｮ蛻�蜑ｲ譁�蟄励ｒ謾ｹ陦梧枚蟄励↓鄂ｮ謠幢ｼ�split縺励◆縺ｨ縺阪↓縲後ゅ阪↑縺ｩ縺ｮ諠�蝣ｱ繧堤┌縺上＆縺ｪ縺�縺溘ａ�ｼ�
        text = re.sub(r"({})".format(delimiter), r"\1\n", text)

        # 謾ｹ陦梧枚蟄励〒蛻�蜑ｲ
        sentences = text.splitlines()

        # 蜑榊ｾ後�ｮ遨ｺ逋ｽ譁�蟄励ｒ蜑企勁
        sentences = [sentence.strip() for sentence in sentences]

        return sentences

    def _morphological_analysis(self, sentence):
        morphemes = []
        node = self.tagger.parseToNode(sentence)
        while node:
            if node.posid != 0:
                morpheme = node.surface
                morphemes.append(morpheme)
            node = node.next
        return morphemes

    def _make_triplet(self, morphemes):
        # 3縺､邨�繧偵▽縺上ｌ縺ｪ縺�蝣ｴ蜷医�ｯ邨ゅ∴繧�
        if len(morphemes) < 3:
            return {}

        # 蜃ｺ迴ｾ蝗樊焚縺ｮ霎樊嶌
        triplet_freqs = defaultdict(int)

        # 郢ｰ繧願ｿ斐＠
        for i in range(len(morphemes) - 2):
            triplet = tuple(morphemes[i:i + 3])
            triplet_freqs[triplet] += 1

        # begin繧定ｿｽ蜉�
        triplet = (PrepareChain.BEGIN, morphemes[0], morphemes[1])
        triplet_freqs[triplet] = 1

        # end繧定ｿｽ蜉�
        triplet = (morphemes[-2], morphemes[-1], PrepareChain.END)
        triplet_freqs[triplet] = 1

        return triplet_freqs

    def save(self, triplet_freqs, init=False):
        # DB繧ｪ繝ｼ繝励Φ
        con = sqlite3.connect(PrepareChain.DB_PATH)

        # 蛻晄悄蛹悶°繧牙ｧ九ａ繧句�ｴ蜷�
        if init:
            # DB縺ｮ蛻晄悄蛹�
            with open(PrepareChain.DB_SCHEMA_PATH, "r") as f:
                schema = f.read()
                con.executescript(schema)

            # 繝�繝ｼ繧ｿ謨ｴ蠖｢
            datas = [(triplet[0], triplet[1], triplet[2], freq)
                     for (triplet, freq) in triplet_freqs.items()]

            # 繝�繝ｼ繧ｿ謖ｿ蜈･
            p_statement = u"insert into chain_freqs (prefix1, prefix2, suffix, freq) values (?, ?, ?, ?)"
            con.executemany(p_statement, datas)

        # 繧ｳ繝溘ャ繝医＠縺ｦ繧ｯ繝ｭ繝ｼ繧ｺ
        con.commit()
        con.close()

    def show(self, triplet_freqs):
        for triplet in triplet_freqs:
            print("|".join(triplet), "\t", triplet_freqs[triplet])


if __name__ == "__main__":
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close()
    chain = PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)
