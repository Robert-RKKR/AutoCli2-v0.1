<script setup lang="ts">
</script>

<template>
    <div class="box_container">

        <article class="box_item">
            <!-- <div class="box_item_head"></div> -->
            <div class="box_item_body">
                <form class="object_form">
                    <div class="object_form_item">
                        <label for="fname">First name:</label>
                        <input type="text" id="fname" name="fname">
                    </div>
                    <div class="object_form_item">
                        <label for="lname">Last name:</label>
                        <input type="text" id="lname" name="lname">
                    </div>
                    <div class="object_form_item">
                        <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
                        <label for="vehicle3"> I have a boat</label>
                    </div>
                    <div class="object_form_item">
                        <label for="country">Country: </label>
                        <select name="country" id="country">
                            <option>Select an option</option>
                            <option value="nepal">Nepal</option>
                            <option value="usa">USA</option>
                            <option value="australia">Australia</option>
                        </select>
                    </div>
                </form>
            </div>
            <!-- <div class="box_item_footer"></div> -->
        </article>

    </div>
</template>

<style scoped>
    .box_item {
        background: #e0dfdf;
    }

    .box_item_head,
    .box_item_body,
    .box_item_footer {
        padding: 30px;
    }

    .object_form {
        display: flex;
        flex-direction: row;
        justify-content	: space-between;
    }
</style>
