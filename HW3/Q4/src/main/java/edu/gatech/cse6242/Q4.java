package edu.gatech.cse6242;

import java.util.StringTokenizer;
import java.lang.Object;


import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

public class Q4 {
	public static class FreqMapper extends Mapper<Object, Text, IntWritable, IntWritable>{
		private IntWritable frequency = new IntWritable();
		private IntWritable one = new IntWritable(1);
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
			StringTokenizer it = new StringTokenizer(value.toString(), "\n");
			while(it.hasMoreTokens()){
				String line = it.nextToken();
				String tokens[] = line.split("\t");
				frequency.set(Inter.parseInt(tokens[1]));
				context.write(frequency, one);

			}
		}
	}
	public static class MapGraph extends Mapper<Object, Text, IntWritable, IntWritable>{
		private IntWritable source = new IntWritable();
		private IntWritable target = new IntWritable();
		private IntWritable add = new IntWritable(1);
		private IntWritable minus = new IntWritable(-1);
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
			StringTokenizer it = new StringTokenizer(Value.toString(), "\n");
			while(it.hasMoreTokens()){
				String line = it.nextToken();
				String tokens[] = line.split("\t");

				source.set(Integer.parseInt(token[0]));
				target.set(Integer.parseInt(tokens[1]));
				context.write(source, add);
				context.write(target, minus);
			}
		}
	}

	public static class ReduceGraph extends Reducer<IntWritable, IntWritable, IntWritable, IntWritable>{
		public void reduce(IntWritable key, IntWritable<IntWritable> values, Context context) throws IOException, InterruptedException{
			int count = 0;
			for (IntWritable value: values){
				count += value.get();
			}
			context.write(key, new IntWritable(count));
		}
	}


  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "Q4");

    /* TODO: Needs to be implemented */
    job.setJarByClass(Q4.class);
    job.setMapperClass(MapGraph.class);
    job.setCombinerClass(ReduceGraph.class);
    job.setReducerClass(ReduceGraph.class);
    job.setOutputKeyClass(IntWritable.class);
    job.setOutputValueClass(IntWritable.class);

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path("First_out"));

    job.waitForCompletion(true);

    Job job2 = Job.getInstance(conf, "job2");
    job2.setJarByClass(Q4.class);
    job2.setMapperClass(FreqMapper.class);
    job2.setCombinerClass(ReduceGraph.class);
    job2.setReducerClass(ReduceGraph.class);
    job2.setOutputKeyClass(IntWritable.class);
    job.2setOutputValueClass(IntWritable.class);

    FileInputFormat.addInputPath(job2, new Path("First_out"));
    FileOutputFormat.setOutputPath(job2, new Path(args[1]));

    System.exit(job2.waitForCompletion(true) ? 0 : 1);
  }
}
