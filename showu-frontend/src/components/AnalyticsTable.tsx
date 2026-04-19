// src/components/AnalyticsTable.tsx

export default function AnalyticsTable({ data }: { data: any[] }) {
  return (
    <table className="analytics-table">
      <thead>
        <tr>
          <th>User</th>
          <th>Action</th>
          <th>Post/Video</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        {data.map((entry: any) => (
          <tr key={entry.id}>
            <td>{entry.user_id}</td>
            <td>{entry.action}</td>
            <td>{entry.post_id || entry.video_id}</td>
            <td>{new Date(entry.created_at).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}