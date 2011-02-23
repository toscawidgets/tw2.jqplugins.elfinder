<%namespace name="tw" module="tw2.core.mako_util"/>
<textarea ${tw.attrs(attrs=w.attrs)}>${w.value or ''}</textarea>
<script type="text/javascript">
$(function() {
    $("#${w.selector}").elfinder(${w.options});
});
</script>

