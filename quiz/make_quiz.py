#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseフォルダのファイルを加工して問題に変換する
"""
    重要：適当に問題を生成しています。
        大体100近いファイルを一気に作成します。
        
    ※lv=レベル
    ※加工ファイル名はプログラムに埋め込んでいる（make_quiz関数）
    ※自分にできるところから始める
    
    基本的にはlv が大きいほど消えている量が多くて難しくなる。
    lvが違うけど、同じ結果になっていたりするかもしれない。

    基本的に自分のやりやすいレベルから始める。
        難しかったらレベルを下げてみる。
        全部やる必要はない。いきなり空白のファイルから試してもいい。
        lv01 がやさしかったら、lv50 まで進んでもいい。
        
    記憶術で記憶してテキストを埋めていくのが基本だけど
    ・単語のスペルを書く能力
    ・英文を推測する能力
    で埋めてもいい。

    ・ヒントの情報がじゃまなとき
        ・一度、改行を入力してから回答を入力して、その後ヒントを消します。
        ・もしくはヒントの無いlinenumberonelyを使います。
    
        

    lv01 スペースを消す
        単語の間にスペースを入れて元の文章を構成すればOK
        もしくは見ながらスペースを入れながら打ち込む
        
    lv02 行の最初の単語、最後の単語はそのまま 
    lv03 行の最初の単語はそのまま
    lv04 行の全ての単語を入れ替える
        lv02,lv03,lv04は単語の入れ替え
            単語のスペルの能力は不要
        テキストベースの入れ替えはめんどくさかった。

    lv05以上は単語のスペルの能力が必要

    lv05 母音をマスクする
    lv06 子音をマスクする
    lv07 記号をマスクする
    lv08 母音＋記号をマスクする
    lv09 子音＋記号をマスクする
    
        母音と子音をそれぞれにかけるなら元の英文を構成できるかも

    lv10 単語の最後の文字をマスクする
        lv10-1文字をマスクする  <-割とやさしい
        lv11-2文字をマスクする
        lv19だとほとんどの単語がマスクされている

    lv20 単語の先頭の文字をマスクする
        lv20-1文字マスクする  <-割とやさしい
        lv21-2文字マスクする
        lv29だとほとんどの単語がマスクされている

    lv30 短い単語をマスクする
        lv30 短い単語を1単語以上マスクする
        lv31 短い単語を2単語以上マスクする
        lv39 短い単語を10単語以上マスクする
        ※to the and などの短い単語からマスクしていくので構文の訓練になります。

    lv40 長い単語をマスクする
        lv40 長い単語を1単語以上マスクする
        lv41 長い単語を2単語以上マスクする
        lv49 長い単語を10単語以上マスクする
        ※長い単語の訓練になります。
        
    ※lv30,lv40台は　マスクする文字数を算出して、その文字数までの単語をマスクします。lv40,lv41が同じ結果になっていることもあります。

    lv50 aの文字をマスクする
        lv05よりも簡単になっている・・・
        a　をいれていくだけ
    lv51 a,bの文字をマスクする
        a,b　をいれていくだけ
    lv52 a,b,cの文字をマスクする
    lv65 a-z の文字をマスクする
        ほとんどの文字がマスクされています。
        lv90よりも難しいかもしれません。
        マスクする文字が増えるごとに、急激に難易度があがります。
        内容的に続きのレベルにしたかったのでlv50-lv65にまとめました。
        
    lv66 先頭の単語を残して単語をいくつかマスクする
        lv66-69 行 単語をマスクする量が増えていく


    lv70 偶数番の単語をマスクする
    lv71 奇数番の単語をマスクする
        lv30台、lv40台でほとんどマスクされているケースよりもこちらのほうがやさしいかもしれません。
        lv70,lv71　を組み合わせると元の文章が構成できる
    
    lv72 1,5,9 4n+1 の単語だけを残して単語をマスクする
    lv73 1,9,17 8n+1 の単語だけを残して単語をマスクする
    lv74 1,9,17 8n+1 の単語だけをマスクして、他は残す
    lv75 1,5,9 4n+1 の単語だけをマスクして、他は残す
    ※1,5,9,...,4n+1　と1,9,17,...,8n+1 は特殊扱いしています。
    ※自分が使っている記憶術の「Pippa's Songを記憶する八方向記憶術」「Mnemonics-8Way-Pro」で特徴的な位置にある単語のためです。
    
    lv76 1,5,9 4n+1 の単語だけを残して単語をマスクする
    lv77 lv76の一部を空行にする
        lv77-lv79        
    lv80 先頭の単語のみ
        81-89 
            81は一行おきに先頭の単語がある
            92は二行おきに先頭の単語がある

    lv90 先頭の文字のみ
        91-97
            91は一行おきに先頭の文字
            92は二行おきに先頭の文字
            
    lv98 linenumber のみ

    lv99 空白のファイルになる
    
    ある程度記憶したらlv100に挑戦してもいいです。
    lv100 空白のファイルにダイジェストを書ける
        書き換えの訓練をしてください。
        ・名詞を置き換える
        ・動詞を置き換える
        ・主語を置き換える
        ・述語を置き換える

"""
import os
import random

# MASK_CHAR:マスクに使用する文字 

# 空白にするとマスクが空白になる
# MASK_CHAR=" "

# ""にするとマスクではなく削除になる
# MASK_CHAR=""

MASK_CHAR="_"

FLAG_ANSWER=False

def empty_line(w_line):
    """
    """
        
    return "empty_line"


def makedirs(dir_make):
    up_dir_make = os.path.abspath(dir_make).upper()
    if os.path.isdir(dir_make):
        return
    return os.makedirs(dir_make)

def get_mask_alphabet_lv50(lv):
    """
    lv50で使用するマスク用の文字の集合を返す
    lv50 -> a,A
    lv51 -> a,b,A,B
    """
    w_mask_char=list()
    w_del_char_l=[chr(i) for i in range(97, 97+(lv-50)+1)] # a,b
    w_del_char_u=[chr(i) for i in range(65, 65+(lv-50)+1)] # A,B
    w_mask_char.extend(w_del_char_l)
    w_mask_char.extend(w_del_char_u)
    return w_mask_char

def get_all_alphabet():
    """
    アルファベットの集合を返す a-z,A-Z
    """
    w_mask_char=list()
    w_del_char_l=[chr(i) for i in range(97, 97+26+1)]
    w_del_char_u=[chr(i) for i in range(65, 65+26+1)]
    w_mask_char.extend(w_del_char_l)
    w_mask_char.extend(w_del_char_u)
    return w_mask_char

def get_vowel():
    """
    母音を返す
    """
    return ["a","i","u","e","o","A","I","U","E","O"]

def get_all_symbol():
    """
    子音を返す
    """
    return ["!",'"',".","'","?",":",";","-",",",")","("]

def get_vowel_symbols():
    return get_vowel()+get_all_symbol()
    
def get_consonant_symbol():
    return set(get_consonant()).union(set(get_all_symbol()))

def get_consonant():
    return set(get_all_alphabet())-set(get_vowel())

def is_memory_line(line_info):
    """
    記憶対象の行かを確認する
    行番号. 文章 の構成になっているか
    """
    if len(line_info)!=2:
        # 行番号＋文章の構成でない
        return False

    if line_info[1].strip()=="":
        # 行番号＋文章の構成だけど 文章が空
        return False
    return True

def proc_txt_lv01_del_space(lines,lv):
    """
        lv01 スペースを消す
    """
    w_ret=list()
    
    wcount=0
    
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+line_info[1].replace(" ","")
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret

def dum_rand(max_rnd,i):
    """乱数っぽいなにか"""
    return ((max_rnd * 3+5 ) *7+i*2) % max_rnd 

def my_shuffle(wlist):
    if False:
        #　動かすたびにlv02,lv03,lv04の結果がランダムになる
        # githubにアップする結果が毎回変わるので固定にするために擬似的なシャッフルを作成
        w_new_list=wlist[:]
        random.shuffle(w_new_list)
        return w_new_list
    else:
        #　lv02,lv03,lv04の結果が固定になる。ランダムではないシャッフル
        w_tmp_list=wlist[:]
        
        for i in range(0,len(w_tmp_list)):
            j=dum_rand(len(w_tmp_list),i)
            tmp=w_tmp_list[i]
            w_tmp_list[i]=w_tmp_list[j]
            w_tmp_list[j]=tmp
            #print("i,j:",i,j)
            #print("w_tmp_list:",w_tmp_list)
        return w_tmp_list
    
def proc_txt_lv02_swap_line(lines,lv):
    """
        lv02 行の最初の単語、最後の単語はそのまま 
        単語の入れ替え
            単語のスペルの能力は不要
    """
    w_ret=list()
    
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            wele=line_info[1].split(" ")
            if len(wele)>=4:
                w_new_ele=list()
                w_new_ele.append(wele[0])
                w_shuffle_ele=wele[1:-1]
                w_shuffle_ele=my_shuffle(w_shuffle_ele ) #入れ替え
                w_new_ele.extend(w_shuffle_ele)
                w_new_ele.append(wele[-1])
                wele=w_new_ele        
            w_new_line=line_info[0]+" "+" ".join(wele)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv03_swap_line(lines,lv):
    """
    lv03 行の最初の単語はそのまま
        単語の入れ替え
    """
    w_ret=list()
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            wele=line_info[1].split(" ")
            if len(wele)>=3:
                w_new_ele=list()
                w_new_ele.append(wele[0])
                #w_new_ele.append(my_shuffle( wele[1:])) # 入れ替え
                w_shuffle_ele=wele[1:]
                w_shuffle_ele=my_shuffle(w_shuffle_ele )
                w_new_ele.extend(w_shuffle_ele)
                wele=w_new_ele
            
            w_new_line=line_info[0]+" "+" ".join(wele)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv04_swap_line(lines,lv):
    """
    lv04 行の全ての単語を入れ替える
            単語のスペルの能力は不要
    """
    w_ret=list()
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            wele=line_info[1].split(" ")
            wele=my_shuffle(wele)    # 入れ替え
            
            w_new_line=" ".join(wele)
            w_new_line=line_info[0]+w_new_line
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv05_mask_vowel(lines,lv):
    """
    lv05以上は単語のスペルの能力が必要

    lv05 母音をマスクする
    """
    w_ret=list()
    
    wcount=0
    w_mask_char=get_vowel() # 母音の文字集合
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask(line_info[1],w_mask_char)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv06_mask_consonant(lines,lv):
    """
    lv06 子音をマスクする
    """
    w_ret=list()
    
    wcount=0
    w_mask_char=get_consonant() # 子音の文字集合
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask(line_info[1],w_mask_char)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv07_mask_symbol(lines,lv):
    """
    lv07 記号をマスクする
    """
    w_ret=list()
    
    wcount=0
    w_mask_char=get_all_symbol()
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask(line_info[1],w_mask_char)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
    
def proc_txt_lv08_mask_vowel_symbol(lines,lv):
    """
    lv08 母音＋記号をマスクする
    """
    w_ret=list()
    
    w_mask_char=get_vowel_symbols()
    wcount=0
    
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask(line_info[1],w_mask_char)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
            
    
def proc_txt_lv09_mask_consonant_symbol(lines,lv):
    """
    lv09 子音＋記号をマスクする
    """
    w_ret=list()
    
    wcount=0
    w_mask_char=get_consonant_symbol()
    
    
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask(line_info[1],w_mask_char)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret

def proc_line_mask_last_letter(line,wdelcnt):
    """
    単語の文字を後ろからマスクする
    """
    w_words = line.split(" ")
    wret=list()
    for w_word in w_words:
        mask_char=MASK_CHAR*min( wdelcnt,len(w_word))
        wret.append(w_word[0:-wdelcnt]+mask_char)
    return " ".join(wret)                
    
def proc_line_mask_top_letter(line,wdelcnt):
    """
    単語の文字を前からマスクする
    """
    w_words = line.split(" ")
    wret=list()
    for w_word in w_words:
        mask_char=MASK_CHAR*min( wdelcnt,len(w_word))
        wret.append(mask_char+w_word[wdelcnt:])
    return " ".join(wret)                
    
def proc_txt_lv10_19_mask_last_letter(lines,lv):
    """
        lv10 単語の最後の文字をマスクする
        lv10-1文字をマスクする
        lv11-2文字をマスクする
        lv19だとほとんどの単語がマスクされている
    """
    w_ret=list()
    
    wcount=0
    dellen=lv-10+1  #マスクする文字の数
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask_last_letter(line_info[1],dellen)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret    
    
    
def proc_txt_lv20_29_mask_top_letter(lines,lv):
    """
    lv20 単語の先頭の文字をマスクする
        lv20-1文字マスクする
        lv21-2文字マスクする
        lv29だとほとんどの単語がマスクされている
    """

    w_ret=list()
    
    wcount=0
    dellen=lv-20+1 #マスクする文字の数
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask_top_letter(line_info[1],dellen)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret    
        
def proc_line_mask_short_word (line,lv,slv):
    """
    lv30 短い単語をマスクする
        lv30 短い単語を1単語以上マスクする
        lv31 短い単語を2単語以上マスクする
        lv39 短い単語を10単語以上マスクする
    """

    di_len=make_len_dict(line)
    wlenkeys=di_len.keys()
    wlenkeys=sorted(wlenkeys,reverse=False)
    wwordcounter=0
    w_del_count=lv-slv+1
    w_del_len=0
    for wchklen in wlenkeys:
        wwordcounter=wwordcounter+di_len[wchklen]
        if wwordcounter>=w_del_count:
            w_del_len=wchklen
            break
    #if w_del_len==0:
    #    return ""
    w_words=line.split(" ")
    w_ret=list()
    for w_word in w_words:
        if len(w_word)<=w_del_len:
            w_ret.append(MASK_CHAR*len(w_word))
        else:
            w_ret.append(w_word)
    return " ".join(w_ret)
    
    
   
def proc_txt_lv30_39_mask_short_word(lines,lv):
    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask_short_word(line_info[1],lv,30)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret    

    
        
def make_len_dict(line):
    w_words=line.split(" ")
    di_len=dict()
    for wele in w_words:
        wlen=len(wele)
        if wlen not in di_len:
            di_len[wlen]=0
        di_len[wlen]=di_len[wlen]+1
    return di_len
    
def proc_line_mask_long_word(line,lv,slv):
    di_len=make_len_dict(line)
    wlenkeys=di_len.keys()
    wlenkeys=sorted(wlenkeys,reverse=True)
    wwordcounter=0
    w_del_count=lv-slv+1
    w_del_len=0
    for wchklen in wlenkeys:
        wwordcounter=wwordcounter+di_len[wchklen]
        if wwordcounter>=w_del_count:
            w_del_len=wchklen
            break
    ##if w_del_len==0:
    #    return ""
    w_words=line.split(" ")
    w_ret=list()
    for w_word in w_words:
        if len(w_word)>=w_del_len:
            w_ret.append(MASK_CHAR*len(w_word))
        else:
            w_ret.append(w_word)
    wretstr= " ".join(w_ret)
    return wretstr
    
def proc_txt_lv40_49_mask_long_word(lines,lv):
    """
    lv40 先頭の単語は残して、長い単語をマスクする
        lv40 長い単語を1単語以上マスクする
        lv41 長い単語を2単語以上マスクする
        lv49 長い単語を10単語以上マスクする
    """


    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask_long_word(line_info[1],lv,40)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret    

    
def proc_line_mask(line,w_mask_char):
    wret=list()
    for wletter in line:
        if wletter!=" " and wletter in w_mask_char:
            wret.append(MASK_CHAR)
        else:
            wret.append(wletter)
    return "".join(wret)
    
def proc_txt_lv50_65_mask_letter_abc(lines,lv):
    """
    lv50 aの文字をマスクする
        lv05よりも簡単になっている・・・
    lv51 a,bの文字をマスクする
    lv65 a-z の文字をマスクする
    """

    w_ret=list()
    
    wcount=0
    w_mask_char=get_mask_alphabet_lv50(lv)
    
    
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_mask(line_info[1],w_mask_char)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_line_word_mask(line,lv,slv):
    w_words=line.split(" ")
    w_new_words=list()
    wordcount=1
    
    for w_word in w_words:
        if((wordcount+1)%(lv-slv+2)==1) or wordcount==1:
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wordcount=wordcount+1
    return " ".join(w_new_words)                

    
def proc_txt_lv66_69_mask_word(lines,lv):
    """
    
    lv66 先頭の単語を残して単語をいくつかマスクする
        lv66-69 行 単語をマスクする量が増えていく
    """

    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_word_mask(line_info[1],lv,66)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
def proc_txt_lv70_even_word(lines,lv):

    """
    lv70 偶数番の単語をマスクする
        lv30台、lv40台でほとんどマスクされているケースよりもこちらのほうがやさしいかも
    """

    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_even_word(line_info[1])
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret


def proc_line_even_word(line):
    w_words=line.split(" ")
    w_new_words=list()
    wcount = 1
    for w_word in w_words:
        if(wcount%2!=0):
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wcount =wcount +1
    return " ".join(w_new_words)                

    
def proc_txt_lv71_odd_word(lines,lv):
    """
    lv71 奇数番の単語をマスクする
    """
    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_odd_word(line_info[1])
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    

def proc_line_odd_word(line):
    w_words=line.split(" ")
    w_new_words=list()
    wcount=1
    for w_word in w_words:
        if(wcount%2==0):
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wcount =wcount +1
    return " ".join(w_new_words)                
    
    
def proc_txt_lv72_word_1_5_9(lines,lv):
    """
    lv72 1,5,9 4n+1 の単語だけを残して単語をマスクする
    """
    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_1_5_9(line_info[1])
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
    
def proc_txt_lv73_word_1_9_17(lines,lv):
    """
    lv73 1,9,17 8n+1 の単語だけを残して単語をマスクする
    """
    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_1_9_17(line_info[1])
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv74_mask_word_1_9_17(lines,lv):
    """
    lv74 1,9,17 8n+1 の単語だけをマスクして、他は残す
    """
    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_del_1_9_17(line_info[1])
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret

    
def proc_txt_lv75_mask_word_1_5_9(lines,lv):
    """
    lv75 1,5,9 4n+1 の単語だけをマスクして、他は残す
    """
    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_del_1_5_9(line_info[1])
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    
def proc_line_1_9_17(line):
    w_words=line.split(" ")
    w_new_words=list()
    wcount=1
    for w_word in w_words:
        if(wcount%8==1):
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wcount=wcount+1
    return " ".join(w_new_words)            
    
    
def proc_line_del_1_9_17(line):
    w_words=line.split(" ")
    w_new_words=list()
    wcount=1
    for w_word in w_words:
        if(wcount%8!=1):
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wcount=wcount+1
    return " ".join(w_new_words)            


def proc_line_del_1_5_9(line):
    w_words=line.split(" ")
    w_new_words=list()
    wcount=1
    for w_word in w_words:
        if(wcount%4!=1):
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wcount=wcount+1
    return " ".join(w_new_words)            
    
def proc_line_1_5_9(line):
    w_words=line.split(" ")
    w_new_words=list()
    wcount=1
    for w_word in w_words:
        if(wcount%4==1):
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
            
        wcount=wcount+1
        
    return " ".join(w_new_words)            
    
def proc_txt_lv76_79_mask_word_1_5_9_and_empty_line(lines,lv):
    """

    lv76 1,5,9 4n+1 の単語だけを残して単語をマスクする
        lv77からときどき空行
    """

    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            if is_empty_line(wcount,lv,76):
                w_ret.append(line_info[0]+" ")
            else:
                w_new_line=line_info[0]+" "+proc_line_1_5_9(line_info[1])
                w_ret.append(w_new_line)
            wcount = wcount + 1
        else:
            w_ret.append(line.strip())
    return w_ret
    
    
def proc_txt_lv80_89_top_word_skip_line(lines,lv):
    """
    lv80 先頭の単語のみ
        81-89 
            81は一行おきに先頭の単語がある
            92は二行おきに先頭の単語がある
    """
    
    w_ret=list()
    
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            if is_empty_line(wcount,lv,80):
                w_ret.append(line_info[0]+" ")
            else:
                w_new_line=line_info[0]+" "+line_info[1].split(" ")[0]
                w_ret.append(w_new_line)
            wcount=wcount+1
        else:
            w_ret.append(line.strip())
    return w_ret
    
def is_empty_line(wcount,lv,s_lv):
    if(lv == s_lv):
        return False
    return (wcount+1)%(lv - s_lv+1)!=1

    
def proc_txt_lv90_97_top_letter_skip_line(lines,lv):
    """
        lv90 先頭の文字のみ
        91-97
            91は一行おきに先頭の文字
            92は二行おきに先頭の文字
    """            
        
    w_ret=list()
    
    #debug
    #chk_is_skip()
    #return w_ret 
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            if is_empty_line(wcount,lv,90):
                w_ret.append(line_info[0]+" ")
            else:
                w_new_line=line_info[0]+" "+line_info[1][0]
                w_ret.append(w_new_line)
            wcount=wcount+1
        else:
            w_ret.append(line.strip())    
        
    return w_ret
    
    
    
def line_to_number_body_pair(wline):
    w_word=wline.strip().split(".")
    w_line_number=w_word[0]+"."
    w_line_body=".".join(w_word[1:]).strip()
    return (w_line_number ,w_line_body)

    
def proc_txt_lv98_line_number_onley(lines,lv):
    """
        lv98 linenumber のみ
    """
    w_ret=list()
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_ret.append(line_info[0])
        else:
            w_ret.append(line.strip())
    return w_ret
    
def proc_txt_lv99_empty_file(lines,lv):
    """
        lv99 空白のファイルになる
    """
    
    return []



def write_quiz_file(li_quiz,lv,w_chap_file_name,w_quiz_dir_suffix=""):    
    """
    """
    
    slv=str(lv)
    if len(slv)==1:
        slv="0"+slv
    f_suffix,w_li_quiz_text=li_quiz
    
    if FLAG_ANSWER:
        fn_quiz="./quiz-a"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    else:
        fn_quiz="./quiz"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    fn_quiz_dir=os.path.dirname(fn_quiz)
    makedirs(fn_quiz_dir)
    
    f=open(fn_quiz,"w")
    txt_write="\n".join(w_li_quiz_text)
    txt_write="Lv"+str(lv)+"-"+f_suffix+"\n"+txt_write +"\n"
    f.write(txt_write)
    f.close()
    
def make_quiz_line(lines,lv):
    if lv==1:
        return ("space",proc_txt_lv01_del_space(lines,lv))
    if lv==2:
        return ("swap",proc_txt_lv02_swap_line(lines,lv))
    if lv==3:
        return ("swap",proc_txt_lv03_swap_line(lines,lv))
    if lv==4:
        return ("swap",proc_txt_lv04_swap_line(lines,lv))
    if lv==5:
        return ("mask_vowel",proc_txt_lv05_mask_vowel(lines,lv))
    if lv==6:
        return ("mask_consonant",proc_txt_lv06_mask_consonant(lines,lv))
    if lv==7:
        return ("mask_symbol",proc_txt_lv07_mask_symbol(lines,lv))
    if lv==8:
        return ("mask_vowel_symbol",proc_txt_lv08_mask_vowel_symbol(lines,lv))
    if lv==9:
        return ("mask_consonant_symbol",proc_txt_lv09_mask_consonant_symbol(lines,lv))

    if lv in range(10,19+1):
        return ("mask_last_letter",proc_txt_lv10_19_mask_last_letter(lines,lv))

    if lv in range(20,29+1):
        return ("mask_top_letter",proc_txt_lv20_29_mask_top_letter(lines,lv))

    if lv in range(30,39+1):
        return ("mask_short_word",proc_txt_lv30_39_mask_short_word(lines,lv))

    if lv in range(40,49+1):
        return ("mask_long_word",proc_txt_lv40_49_mask_long_word(lines,lv))

    if lv in range(50,65+1):
        return ("mask_letter",proc_txt_lv50_65_mask_letter_abc(lines,lv))

    if lv in range(66,69+1):
        return ("mask_word",proc_txt_lv66_69_mask_word(lines,lv))

    if lv ==70:
        return ("even",proc_txt_lv70_even_word(lines,lv))

    if lv ==71:
        return ("odd",proc_txt_lv71_odd_word(lines,lv))

    if lv ==72:
        return ("1_5_9",proc_txt_lv72_word_1_5_9(lines,lv))
    
    if lv ==73:
        return ("1_9_17",proc_txt_lv73_word_1_9_17(lines,lv))

    if lv ==74:
        return ("1_9_17",proc_txt_lv74_mask_word_1_9_17(lines,lv))

    if lv ==75:
        return ("mask_1_5_9",proc_txt_lv75_mask_word_1_5_9(lines,lv))

    if lv in range(76,79+1):
        return ("mask_1_5_9_empty",proc_txt_lv76_79_mask_word_1_5_9_and_empty_line(lines,lv))

    if lv in range(80,89+1):
        return ("top_word",proc_txt_lv80_89_top_word_skip_line(lines,lv))
    
    if lv in range(90,97+1):
        return ("top_letter",proc_txt_lv90_97_top_letter_skip_line(lines,lv))

    if lv ==98:
        return ("linenumberonley",proc_txt_lv98_line_number_onley(lines,lv))

    if lv ==99:
        return proc_txt_lv99_empty_file(lines,lv)

    
def make_quiz_file(w_dir_root,w_file_suffix):
    """
    フォルダの単語リストを作成
    """
    print("make_quiz_file:",w_dir_root)
    wfiles=os.listdir(w_dir_root)
    for w_chap_file_name in wfiles:
        print("parse file:",w_chap_file_name )
        f=open(os.path.join(w_dir_root,w_chap_file_name),"r")
        lines=f.readlines()
        f.close()

        #for lv in range(66,70):
        for lv in range(1,99):
            w_chap_quiz=make_quiz_line(lines,lv)
            write_quiz_file(w_chap_quiz,lv,w_chap_file_name,w_file_suffix)

def make_quiz_holmes():
    
    make_quiz_file("../holmes/base/SH_01_A_Study_in_Scarlet","SH_01")

    make_quiz_file("../holmes/base/SH_02_The_Sign_of_the_Four","SH_02")

    make_quiz_file("../holmes/base/SH_03_The_Hound_of_the_Baskervilles","SH_03")

    make_quiz_file("../holmes/base/SH_04_The_Valley_of_Fear","SH_04")

    make_quiz_file("../holmes/base/SH_05_The_Adventures_of_Sherlock_Holmes","SH_05")

    make_quiz_file("../holmes/base/SH_06_The_Memoirs_of_Sherlock_Holmes","SH_06")

    make_quiz_file("../holmes/base/SH_07_The_Return_of_Sherlock_Holmes","SH_07")

    make_quiz_file("../holmes/base/SH_08_His_Last_Bow","SH_08")


    
def make_quiz():
    #make_quiz_file("../TheArtOfWar/base","TheArtOfWar")
    make_quiz_file("../TheArtOfWar/base","")
    


    


if __name__=="__main__":
    # The Art Of War
    make_quiz()
    
    # Holmes 
    #make_quiz_holmes()
