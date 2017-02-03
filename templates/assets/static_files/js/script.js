/**
 * Created by avtan on 06.01.2017.
 */

// $('.menu > li:first-child').addClass('link_active');
//
// $('.menu > li').on('click', function (event) {
//     // event.preventDefault();
//     $('.menu > li').removeClass('link_active');
//     $(this).addClass('link_active');
// });

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
    $(this).parent('.f_form').parent('.filter').children('.expanded_filter').show(300);
}

function ClosePopup(){
    $(this).parent('.a_links').parent('.expanded_filter').hide(300);
    $(this).parent('.a_links').parent('.expanded_filter').parent('.filter').children('.filter_form').css('display', 'block');
}

$(document).ready(function () {
    $('.filter').find('.filter_form').children('.close').click(OpenPopup);
    $('.filter').find('.expanded_filter').children('.a_links').children('.close').click(ClosePopup);
});



// �������� ����� ������� � ���������� ����������
$('.pagination > li > a').on('click', function (event) {
    event.preventDefault();
    $('.pagination > li a').removeClass('active');
    $(this).addClass('active');
});

var $blocks = $('.blocks');
var $link_block = $('.link_block');
totalBlocks = $blocks.children('.item').length;
totalBlocks = $link_block.children('.link_item').length;


// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("modal_close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }



}