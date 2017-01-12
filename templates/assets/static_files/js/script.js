/**
 * Created by avtan on 06.01.2017.
 */

$('.slider').slick({
    cssEase: 'ease-in',
    autoplay: true,
    autoplaySpeed: 2000,
    //variableWidth: true,
    arrows: false
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

$(".menu-collapsed").click(function() {
    $(this).toggleClass("menu-expanded");
});



function OpenPopup(){
    $(this).parent('.f_form').css('display', 'none');
    $(this).parent('.f_form').parent('.filter').children('.expanded_filter').css('display', 'block');
}

function ClosePopup(){
    $(this).parent('.a_links').parent('.expanded_filter').css('display', 'none');
    $(this).parent('.a_links').parent('.expanded_filter').parent('.filter').children('.filter_f').css('display', 'block');
}

$(document).ready(function () {
    $('.filter').find('.filter_f').children('.close').click(OpenPopup);
    $('.filter').find('.expanded_filter').children('.a_links').children('.close').click(ClosePopup);
});