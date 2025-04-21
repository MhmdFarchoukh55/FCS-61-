<?php
// Sample tasks array
$tasks = [
    ["title" => "Buy groceries", "status" => "pending", "due" => "2024-04-15"],
    ["title" => "Submit report", "status" => "done", "due" => "2024-04-10"],
    ["title" => "Go jogging", "status" => "pending", "due" => "2024-04-16"],
    ["title" => "Bokk flight", "status" => "done", "due" => "2024-04-8"],
];

function filterByStatus(array $tasks, string $status): array {
    $filtered = [];
    foreach ($tasks as $task) {
        if ($task['status'] === $status) {
            $filtered[] = $task;
        }
    }
    return $filtered;
}
function groupByStatus(array $tasks): array {
    $grouped = [];
    foreach ($tasks as $task) {
        $status = $task['status'];
        if (!isset($grouped[$status])) {
            $grouped[$status] = [];
        }
        $grouped[$status][] = $task;
    }
    return $grouped;
}

echo "Filtered (pending):\n";
print_r(filterByStatus($tasks, "pending"));

echo "\nGrouped by status:\n";
print_r(groupByStatus($tasks));
?>
