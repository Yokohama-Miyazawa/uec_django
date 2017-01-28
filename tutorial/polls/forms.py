from django import forms


class MyForm(forms.Form):
    text = forms.CharField(max_length=100, required=False, label='テキスト')


class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(
        queryset=None,               # 選択肢を保持する
        label='選択肢',               # フォームにつけるラベル
        widget=forms.RadioSelect(),  # フォームの形式
        empty_label=None,            # 「何も選ばない」という選択肢は無し
        error_messages={             # エラーメッセージ
            'required': "選択肢が何も選ばれていません。",
            'invaid_choice': "無効な選択肢です。",
        }
    )

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = question.choice_set.all()
