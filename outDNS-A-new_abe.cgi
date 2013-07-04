#!/usr/local/bin/perl

# get jcode.pl
require 'jcode.pl';

# receive input
# read(STDIN, $input, $ENV{'CONTENT_LENGTH'});

# split, decode and convert
# @pairs = split(/&/, $input);
@pairs = split(/&/, $ENV{'QUERY_STRING'});
foreach (@pairs) {
        ($name, $value) = split(/=/, $_);
        $name  =~ tr/+/ /;
        $value =~ tr/+/ /;
        $name =~ s/%([A-F0-9][A-F0-9])/pack("C", hex($1))/gie;
        $value =~ s/%([A-F0-9][A-F0-9])/pack("C", hex($1))/gie;
        &jcode'convert(*name,'euc');
        &jcode'convert(*value,'euc');
        $field{$name} = $value;
}

print 'Content-type: text/html; charset=EUC-JP', "\n\n";
print '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">', "\n";
print '<html>', "\n";
print '<head>', "\n";
print '<title>社外向けDNS Aレコード登録申請フォーム ～ Internet基本サービス ～</title>', "\n";
print '<meta http-equiv="Content-Style-Type" content="text/css" />', "\n";
print '<meta http-equiv="Content-Script-Type" content="text/javascript" />', "\n";
print '<meta http-equiv="Content-Type" content="text/html; charset=EUC-JP" />', "\n";
print '<link rel="stylesheet" type="text/css" href="http://fxwan.fxis.co.jp/internet/style.css">', "\n";
print '</head>', "\n";
print '<body>', "\n";
print '<div id="dnsForm">', "\n";
print '<h2>社外向けDNS Aレコード登録 申請フォーム</h2>', "\n";
print '<h3>入力 → <span class="form1">確認</span> → 完了</h3>', "\n";

# @args = split(/&/, $ENV{'QUERY_STRING'});
# foreach $arg (@args) {
    # ($name, $val) = split (/=/, $arg);
    # $val =~ s/\+/ /g;
    # $val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack('C', hex($1))/eg;
    # $field{$name} = $val;
# }

if (($field{'company'} eq "") || ($field{'name'} eq "") || ($field{'tel'} eq "") || ($field{'address'} eq "") || ($field{'http'} eq "") || ($field{'https'} eq "") || ($field{'acl'} eq "")){
   err()
}
sub err{
  $msg .= "<div>\n";
  $msg .= "【所属】<br>\n";
  $msg .= "【氏名】<br>\n";
  $msg .= "【内線番号】<br>\n";
  $msg .= "【メールアドレス】<br>\n";
  $msg .= "【HTTP/HTTPS通信の有無】<br>\n";
  $msg .= "【アクセス元制限の有無】<br>\n";
  $msg .= "<br>\n";
  $msg .= "上記については必ず記入して下さい。\n";
#  $msg .= $_[0];
  $msg .= "</div>\n";
  $msg .= "<br>\n";
  $msg .= '<div class="button">';
  $msg .= "\n";
  $msg .= '<input type="button" value="&nbsp;戻る&nbsp;" onclick="history.back();">';
  $msg .= "\n";
  $msg .= "</div>\n";
  $msg .= "</div><!-- dnsForm end -->\n";
  $msg .= "</body>\n";
  $msg .= "</html>";

  &jcode'convert(*msg, "euc");

  print "\n";
  print "$msg\n";

  exit(0);
}


print '<form action="outDNS-A-new-mail_abe.cgi" method="GET">', "\n";
print '<h4>申請者情報</h4>', "\n";
print '<table class="tab1">', "\n";
print '<tr>', "\n";
print '<td class="td2">所属(会社名 部署)</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'company'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">氏名</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'name'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">内線番号</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'tel'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">メールアドレス</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'address'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '</table>', "\n";
print '<h4>申請内容</h4>', "\n";
print '<table class="tab1">', "\n";
print '<tr>', "\n";
print '<td class="td2">ドメイン名</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'domain'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">ホスト名</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'host'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">グローバルIPアドレス</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'new'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">HTTP通信の有無</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'http'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">HTTPS(SSL)通信の有無</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'https'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">HTTPサイト確認用URL</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'URL1'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">HTTPSサイト確認用URL</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'URL2'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">設定希望日</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'date'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '<tr>', "\n";
print '<td class="td2">アクセス元制限の有無</td>', "\n";
print '<td class="td3">', "\n";
print "$field{'acl'}", "\n";
print '</td>', "\n";
print '</tr>', "\n";
print '</table>', "\n";
print '<h4>備考</h4>', "\n";
print '<table>', "\n";
print '<tr>', "\n";
print '<td class="td3"><pre style="margin: 0px;">', "\n";
print "$field{'tokki'}", "\n";
print '</pre></td>', "\n";
print '</tr>', "\n";
print '</table>', "\n";

print "<input type=\"hidden\" name=\"subject\" value=\"$field{'subject'}\">", "\n";
print "<input type=\"hidden\" name=\"company\" value=\"$field{'company'}\">", "\n";
print "<input type=\"hidden\" name=\"name\"    value=\"$field{'name'}\"   >", "\n";
print "<input type=\"hidden\" name=\"tel\"     value=\"$field{'tel'}\"    >", "\n";
print "<input type=\"hidden\" name=\"address\" value=\"$field{'address'}\">", "\n";
print "<input type=\"hidden\" name=\"domain\"  value=\"$field{'domain'}\" >", "\n";
print "<input type=\"hidden\" name=\"host\"    value=\"$field{'host'}\"   >", "\n";
print "<input type=\"hidden\" name=\"new\"     value=\"$field{'new'}\"    >", "\n";
print "<input type=\"hidden\" name=\"http\"    value=\"$field{'http'}\"   >", "\n";
print "<input type=\"hidden\" name=\"https\"   value=\"$field{'https'}\"  >", "\n";
print "<input type=\"hidden\" name=\"URL1\"    value=\"$field{'URL1'}\"   >", "\n";
print "<input type=\"hidden\" name=\"URL2\"    value=\"$field{'URL2'}\"   >", "\n";
print "<input type=\"hidden\" name=\"date\"    value=\"$field{'date'}\"   >", "\n";
print "<input type=\"hidden\" name=\"acl\"     value=\"$field{'acl'}\"    >", "\n";
print "<input type=\"hidden\" name=\"tokki\"   value=\"$field{'tokki'}\"  >", "\n";

print '<hr><br>', "\n";
print '<div class="button">', "\n";
print '<input type="submit" value="&nbsp;申請"&nbsp;>';
print '&nbsp;&nbsp;&nbsp;&nbsp;';
print '<input type="button" value="&nbsp;修正&nbsp;" onclick="history.back();">', "\n";
print '</div>', "\n";
print '</form>', "\n";
print '</div><!-- dnsForm end-->', "\n";
print '</body>', "\n";
print '</html>';
#
