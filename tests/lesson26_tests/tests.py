import pytest

frames_dict_correct = {
    "frame1": "Frame1_Secret",
    "frame2": "Frame2_Secret"
}


@pytest.mark.parametrize("secret_key_check", [(frame, phrase) for frame, phrase in frames_dict_correct.items()],
                         indirect=True)
def test_positive_frame_phrase_check(secret_key_check):
    alert_msg = secret_key_check
    assert alert_msg == "Верифікація пройшла успішно!"


frames_dict_wrong = {
    "frame1": "lalala",
    "frame2": "bombom"
}


@pytest.mark.parametrize("secret_key_check", [(frame, phrase) for frame, phrase in frames_dict_wrong.items()],
                         indirect=True)
def test_negative_frame_phrase_check(secret_key_check):
    alert_msg = secret_key_check
    assert alert_msg == "Введено неправильний текст!"

# @pytest.mark.parametrize("secret_key_check", [("frame3", "lalala")], indirect=True)
# def test_error_raised_for_wrong_frame(secret_key_check):
#     with pytest.raises(NoSuchElementException) as nsf:
#         alert_msg = secret_key_check
