#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    チェッカー    
        ファイルを固定でチェックします。
        
        10点評価
        100点評価
            2つの数字を出力します。
            点数のつけ方が少し違うので一致しません。
            
    自分は日付フォルダにコピーして書き換えて使用する予定です。
        
"""
import os

def makedirs(dir_make):
    up_dir_make = os.path.abspath(dir_make).upper()
    if os.path.isdir(dir_make):
        return
    return os.makedirs(dir_make)


    
def line_to_number_body_pair(wline):
    w_word=wline.strip().split(".")
    w_line_number=w_word[0]+"."
    w_line_body=".".join(w_word[1:]).strip()
    return (w_line_number ,w_line_body)
    
    
def title_to_fn(wstr):
    """
    タイトルの文字列をフォルダ用に変換
        記号を_にする
    """
    
    wstr=wstr.replace(" ","_")            
    wstr=wstr.replace("'","_")            
    wstr=wstr.replace(",","_")            
    wstr=wstr.replace(".","_")            
    wstr=wstr.replace("-","_")            
    return wstr
    

UPPER_A_Z=[chr(i) for i in range(65, 65+26)] # A,B

def suppress_new_line(wstr,wsuppress):
    return wstr.replace(wsuppress, wsuppress.replace("__NEW_LINE__"," "))

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

def get_score_10(w_quiz_line,w_base_line):
    if w_quiz_line.strip()==w_base_line.strip():
        return (None,10)

    w_score=0

    li_q=w_quiz_line.strip().split(" ")
    li_b=w_base_line.strip().split(" ")
    w_miss=list()
    
    w_q_idx=0
    w_b_idx=0
    w_same_count=0
    w_same_count_r=0
    for w_word in li_q:
        if w_q_idx >=len(li_q):
            continue
        if w_b_idx >=len(li_b):
            continue
        
        if li_q[w_q_idx]==li_b[w_b_idx]:
            w_same_count=w_same_count+1
        
        
        
        if li_q[len(li_q)-w_q_idx-1]==li_b[len(li_b)-w_b_idx-1]:
            w_same_count_r=w_same_count_r+1
        w_q_idx=w_q_idx+1
        w_b_idx=w_b_idx+1
    

    w_miss.append(get_diff(w_quiz_line,w_base_line))
        
    if w_same_count_r>w_same_count:
        # 後ろからの一致数、前からの一致数で大きいほうを採用する
        w_same_count=w_same_count_r
    
    w_score=int(w_same_count/len(li_b)*10)
    if li_q[0]==li_b[0]:
        #最初の単語が一致ボーナス
        w_score=w_score+1
    if li_q[-1]==li_b[-1]:
        #最後の単語が一致ボーナス
        w_score=w_score+1
    if len(li_q)==len(li_b[-1]):
        #単語数が一致ボーナス
        w_score=w_score+1
        

    if w_score>9:
        #完全に一致していないので9より上なら9に制限
        return (w_miss,9)
    return (w_miss,w_score)
    
    
def get_diff(w_quiz_line,w_base_line):
    import difflib
    d = difflib.Differ()
     
    diff_x=d.compare([w_base_line.strip()],[w_quiz_line.strip()])
    return "\n".join(diff_x) 
    

def get_score_100(w_quiz_line,w_base_line):
    if w_quiz_line.strip()==w_base_line.strip():
        return (None,100)

    w_score=0

    li_q=w_quiz_line.strip().split(" ")
    li_b=w_base_line.strip().split(" ")
        
    w_q_idx=0
    w_b_idx=0
    w_same_count=0
    w_same_count_r=0
    w_miss=list()
    for w_word in li_q:
        if w_q_idx >=len(li_q):
            continue
        if w_b_idx >=len(li_b):
            continue
            
        if li_q[w_q_idx]==li_b[w_b_idx]:
            w_same_count=w_same_count+1
        

        if li_q[len(li_q)-w_q_idx-1]==li_b[len(li_b)-w_b_idx-1]:
            w_same_count_r=w_same_count_r+1

        w_q_idx=w_q_idx+1
        w_b_idx=w_b_idx+1
    
    if w_same_count_r>w_same_count:
        # 後ろからの一致数、前からの一致数で大きいほうを採用する
        w_same_count=w_same_count_r
    
    w_miss.append(get_diff(w_quiz_line,w_base_line))
    
    print("w_same_count,len(li_b)",w_same_count,len(li_b))
    w_score=int(w_same_count/len(li_b)*100)
    if li_q[0]==li_b[0]:
        #最初の単語が一致ボーナス
        w_score=w_score+1
    if li_q[-1]==li_b[-1]:
        #最後の単語が一致ボーナス
        w_score=w_score+1
    if len(li_q)==len(li_b[-1]):
        #単語数が一致ボーナス
        w_score=w_score+1
        

    if w_score>99:
        #完全に一致していないので99より上なら99に制限
        return (w_miss,99)
    return (w_miss,w_score)
        
    
def make_result(quiz_lines ,base_lines,quiz_base_lines):
    li_ret=list()

    di_quiz=dict()
    di_base=dict()
    li_quiz=list()
    di_summary=dict()
    di_quiz_base=dict()
    #回答の行を辞書に変換
    di_summary["ANSWER_LINE"] = 0
    for quiz_line in quiz_lines:
        line_info=line_to_number_body_pair(quiz_line )
        if is_memory_line(line_info):
            if line_info[0] not in di_quiz:
                #行番号が二重にある可能性
                li_quiz.append(line_info[0] )
            di_quiz[line_info[0]]=line_info[1]
        
    #答えの行を辞書に変換
    for base_line in base_lines:
        line_info=line_to_number_body_pair(base_line  )
        if is_memory_line(line_info):
            di_base[line_info[0]]=line_info[1]
        
    #問題文の行を辞書に変換
    for quiz_base_line in quiz_base_lines:
        line_info=line_to_number_body_pair(quiz_base_line)
        if is_memory_line(line_info):
            di_quiz_base[line_info[0]]=line_info[1]


        
    di_summary["TOTAL-SCORE10"] = 0
    di_summary["TOTAL-SCORE100"] = 0

    #回答の行と答えの行を先頭（最後）から比較して同じ単語がある数
    for w_chk_line_number in li_quiz:
        if w_chk_line_number not in di_base:
            #回答が問題文に存在しない
            li_ret.append("SKIP:"+w_chk_line_number )
            continue

        li_ret.append("-"*20)
        if w_chk_line_number in di_quiz_base:
            if di_quiz_base[w_chk_line_number]==di_quiz[w_chk_line_number]:
                #回答が問題文と一致 → 回答していない
                li_ret.append("SKIP-NO-ANSWER:"+w_chk_line_number )
                continue

        di_summary["ANSWER_LINE"] = di_summary["ANSWER_LINE"] +1

        base_line=di_base[w_chk_line_number]
        quiz_line=di_quiz[w_chk_line_number]
        w_score10=get_score_10(quiz_line,base_line )
        w_score100=get_score_100(quiz_line,base_line )
        if w_score10[1]==10:
            li_ret.append(w_chk_line_number+":OK")
        else:
            # 完全でないときはスコアと元のテキスト、回答のテキストを出力
            li_ret.append(w_chk_line_number)
            #print("w_score10:",w_score10)
            li_ret.append("SCORE10 :"+str(w_score10[1]))
            li_ret.append("SCORE100:"+str(w_score100[1]))
            li_ret.append("base:"+base_line)
            li_ret.append("ans :"+quiz_line)
            li_ret.append("\n".join(w_score10[0]))
            #li_ret.append("miss 100:"+str(w_score10[0]))
        di_summary["TOTAL-SCORE10"] = di_summary["TOTAL-SCORE10"] +w_score10[1]
        di_summary["TOTAL-SCORE100"] = di_summary["TOTAL-SCORE100"] + w_score100[1]
    
    if di_summary["ANSWER_LINE"]!=0:
        di_summary["AVERAGE-SCORE10"] = int(di_summary["TOTAL-SCORE10"] /di_summary["ANSWER_LINE"])
        di_summary["AVERAGE-SCORE100"] = int(di_summary["TOTAL-SCORE100"]  /di_summary["ANSWER_LINE"])
    else:
        di_summary["AVERAGE-SCORE10"] = None
        di_summary["AVERAGE-SCORE100"] = None
    

    li_ret.append("-"*20)
    li_ret.append("回答行数:"+str(di_summary["ANSWER_LINE"] ))
    li_ret.append("10点評価:"+str(di_summary["AVERAGE-SCORE10"] ))
    li_ret.append("100点評価:"+str(di_summary["AVERAGE-SCORE100"] ))
             
    return (di_summary,li_ret)
    
def make_check_result(quiz_folder,base_folder,result_folder,quiz_base_folder):
    """
    Quizの回答の結果をチェック
    """
    #ret_li=list()
    makedirs(result_folder)
    print("chk_quiz_file:",quiz_folder)
    wfiles=os.listdir(quiz_folder)
    di_chap_summary=dict()
    for w_chap_file_name in wfiles:
        print("parse file:",w_chap_file_name )
        # 回答を書き込んだファイルを読み込み
        w_quiz_file=os.path.join(quiz_folder,w_chap_file_name)
        if os.path.isdir(w_quiz_file):
            print("SKIP DIR:",w_quiz_file)
            continue

        f=open(w_quiz_file,"r")
        quiz_lines=f.readlines()
        f.close()
        
        
        
        w_base_file=os.path.join(base_folder,w_chap_file_name)
        if os.path.isfile(w_base_file):
            #覚えた対象のファイルを読み込み
            f=open(w_base_file,"r")
            base_lines=f.readlines()
            f.close()
            
            quiz_base_file=os.path.join(quiz_base_folder,w_chap_file_name)
            if os.path.isfile(quiz_base_file):
                print("base-quiz:"+quiz_base_file)
                f=open(quiz_base_file,"r")
                quiz_base_lines=f.readlines()
                f.close()
            else:
                print("base-quiz not exist:"+quiz_base_file)
                quiz_base_lines=list()
            
            
            #結果をファイル毎に書き込み
            ret_one=make_result(quiz_lines,base_lines,quiz_base_lines)
            di_chap_summary[w_chap_file_name]=ret_one[0]
            
            result_one_file=os.path.join(result_folder,"result-"+w_chap_file_name)
            f=open(result_one_file,"w")
            ret_txt="\n".join(ret_one[1])
            #ret_txt="\n".join(ret_one[1])
            f.write(ret_txt)
            f.close()
            
        else:
            print("SKIP FILE:"+w_base_file)
    

    #要約の作成
    
    li_write=list()
    for w_chap_file_name in wfiles:
        if w_chap_file_name in di_chap_summary:
            li_summary=di_chap_summary[w_chap_file_name]
            li_write.append("-"*20)
            li_write.append("FILE:"+w_chap_file_name)
            li_write.append("ANSER_LINE:"+str(li_summary["ANSWER_LINE"]))
            li_write.append("SCORE10   :"+str(li_summary["AVERAGE-SCORE10"]))
            li_write.append("SCORE100  :"+str(li_summary["AVERAGE-SCORE100"]))
    
    f_summary=os.path.join(result_folder,"result-summary.txt")
    f=open(f_summary,"w")
    ret_txt="\n".join(li_write)
    f.write(ret_txt)
    f.close()

    
    #print("ret_li",ret_li)

    
def main():
    FLAG_DEBUG=False
    if FLAG_DEBUG:
        base_folder="F:/practice/base/TheArtOfWar"
        quiz_folder="F:/practice/daily/2019/201902/20190225_theartofwar/quiz/lv05_mask_vowel"
        quiz_base_folder="F:/practice/daily/2019/201902/20190225_theartofwar/quiz-base/lv05_mask_vowel"
    else:
        #記憶対象のファイル
        base_folder="../../TheArtOfWar/base"
        
        #記憶した結果を書き込んだファイル
        quiz_folder="../../daily/2019/201903/20190302_theartofwar/quiz/lv01_space"
        
        #問題文のファイル
        quiz_base_folder="../../quiz/quiz/lv01_space"
    
    # result のフォルダに結果を書き込みます。
    make_check_result(quiz_folder,base_folder,"result-2",quiz_base_folder)
    

if __name__=="__main__":
    main()
