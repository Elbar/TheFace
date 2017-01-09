/**
 * Created by avtan on 06.01.2017.
 */

$('.slider').slick({
    cssEase: 'ease-in',
    autoplay: true,
    autoplaySpeed: 2000,
    //variableWidth: true,
    arrows: true
});

// Select
$('.slct').click(function () {
    /* ������� ���������� ������ � ���������� */
    var dropBlock = $(this).parent().find('.drop');

    /* ������ ��������: ���� ���������� ���� ����� �� ������ ��� �������*/
    if (dropBlock.is(':hidden')) {
        dropBlock.slideDown();

        /* �������� ������ ����������� select */
        $(this).addClass('active');

        /* �������� � �������� ����� �� ��������� ����������� ������ */
        $('.drop').find('li').click(function () {

            /* ������� � ���������� HTML ��� ��������
             ������ �� �������� �������� */
            var selectResult = $(this).html();

            /* ������� ��� ������� ����� � �������� � ����
             �������� �� ���������� selectResult */
            $(this).parent().parent().find('input').val(selectResult);

            /* �������� �������� ���������� selectResult � ������ �������
             ��������� ��� ���������� ������ � ������� ���������� */
            $(this).parent().parent().find('.slct').removeClass('active').html(selectResult);

            /* �������� ���������� ���� */
            dropBlock.slideUp();
        });

        /* ���������� ��������: ���� ���������� ���� �� ����� �� �������� ��� */
    } else {
        $(this).removeClass('active');
        dropBlock.slideUp();
    }

    /* ������������� ������� ��������� ������ ��� ����� */
    return false;
});